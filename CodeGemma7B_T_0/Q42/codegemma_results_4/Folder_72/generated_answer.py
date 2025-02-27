def prime_factors(nums):
    return {factor for factor in range(2, nums[16] + 1) if nums[16] % factor == 0}