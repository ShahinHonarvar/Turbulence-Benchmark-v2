def prime_factors(nums):
    return {factor for factor in set(range(2, nums[51] + 1)) if nums[51] % factor == 0}