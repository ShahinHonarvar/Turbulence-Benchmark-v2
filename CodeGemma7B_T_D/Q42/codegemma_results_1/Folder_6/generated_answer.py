from functools import reduce

def prime_factors(nums):
    return set(reduce(lambda x, y: x * y, nums))