def prime_factors(nums):
    return {factor for factor in range(2, nums[99] + 1) if nums[99] % factor == 0}