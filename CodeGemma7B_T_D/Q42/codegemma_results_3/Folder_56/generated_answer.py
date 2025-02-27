from functools import reduce

def prime_factors(nums):
    return {reduce(lambda a, b: a * b, [n for n in nums if n % nums[60] == 0])}