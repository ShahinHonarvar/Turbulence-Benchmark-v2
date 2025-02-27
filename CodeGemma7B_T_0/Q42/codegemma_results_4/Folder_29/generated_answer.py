def prime_factors(nums):
    return {factor for factor in range(2, nums[19] + 1) if nums[19] % factor == 0}