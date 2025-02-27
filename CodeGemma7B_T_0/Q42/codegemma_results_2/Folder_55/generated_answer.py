def prime_factors(nums):
    return {factor for factor in set(range(2, nums[21] + 1)) if nums[21] % factor == 0}