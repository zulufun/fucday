from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

foods = {1: "Gà kho xả ớt", 2: "Cá lóc kho", 3: "Thịt xào măng", 4: "Bún chả cá"}

@app.get("/api/v1/foods")
async def get_food_by_id(id: int):
    food = foods.get(id)
    if food:
        return {"data": food}
    else:
        raise HTTPException(status_code=404, detail="Food not found")
