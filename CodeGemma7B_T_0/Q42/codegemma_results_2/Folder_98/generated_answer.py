def prime_factors(nums):
    return {factor for factor in range(2, nums[4] + 1) if nums[4] % factor == 0}