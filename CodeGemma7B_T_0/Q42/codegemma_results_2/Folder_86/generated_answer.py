def prime_factors(nums):
    return {factor for factor in set(range(2, nums[194] + 1)) if nums[194] % factor == 0}