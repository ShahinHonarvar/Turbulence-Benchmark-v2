def prime_factors(nums):
    return {factor for factor in range(2, nums[29] + 1) if nums[29] % factor == 0}