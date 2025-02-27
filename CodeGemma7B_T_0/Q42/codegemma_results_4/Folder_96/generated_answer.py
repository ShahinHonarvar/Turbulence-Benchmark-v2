def prime_factors(nums):
    return {factor for factor in range(2, nums[47] + 1) if nums[47] % factor == 0}