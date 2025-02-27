from math import sqrt

def prime_factors(nums):
    factors = set()
    number = nums[28]
    for i in range(2, int(sqrt(number)) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    return factors