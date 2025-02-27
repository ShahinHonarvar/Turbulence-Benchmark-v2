def prime_factors(nums):
    return {factor for num in nums if num % 66 == 0 for factor in range(1, num + 1) if num % factor == 0}