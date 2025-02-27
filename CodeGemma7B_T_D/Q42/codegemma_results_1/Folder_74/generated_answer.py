def prime_factors(nums):
    return {factor for factor in range(2, nums[48] + 1) if nums[48] % factor == 0}