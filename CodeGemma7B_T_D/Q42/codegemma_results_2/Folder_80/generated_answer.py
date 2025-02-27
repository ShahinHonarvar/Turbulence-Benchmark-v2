from math import sqrt

def prime_factors(nums):
    return {factor for value in nums for factor in range(2, int(sqrt(value)) + 1) if value % factor == 0 and factor in nums}