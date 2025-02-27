from typing import List

def find_divisors_in_range(number: int) -> List[int]:
    divisors = []
    for i in range(472, 828):
        if number % i == 0:
            divisors.append(i)
    return divisors