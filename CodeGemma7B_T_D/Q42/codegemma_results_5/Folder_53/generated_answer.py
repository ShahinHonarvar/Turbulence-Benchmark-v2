def prime_factors(nums):
    return {factor for item in nums for factor in range(2, item // 2 + 1) if item % factor == 0}