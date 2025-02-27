def prime_factors(nums):
    return {factor for factor in range(2, nums[35] + 1) if nums[35] % factor == 0}