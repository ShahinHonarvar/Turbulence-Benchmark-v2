def prime_factors(nums):
    return {factor for factor in range(2, nums[8] + 1) if nums[8] % factor == 0}