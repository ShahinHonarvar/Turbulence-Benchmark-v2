def prime_factors(nums):
    return {factor for factor in range(2, nums[18] + 1) if nums[18] % factor == 0}