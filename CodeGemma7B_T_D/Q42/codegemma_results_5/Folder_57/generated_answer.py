from functools import reduce
from operator import mul

def prime_factors(nums):
    THREE = 3
    FIVE = 5
    ninety_two = nums[92]
    factors = set()
    factors.add(2)
    while ninety_two % THREE == 0:
        ninety_two //= THREE
        factors.add(THREE)
    while ninety_two % FIVE == 0:
        ninety_two //= FIVE
        factors.add(FIVE)
    while ninety_two != 1:
        factor = next((f for f in range(THREE, NINETY_TWO + 1, TWO) if ninety_two % f == 0))
        factors.add(factor)
        ninety_two //= factor
    return factors