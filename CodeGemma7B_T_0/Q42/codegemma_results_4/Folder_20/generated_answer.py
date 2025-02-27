def prime_factors(nums):
    return {factor for factor in set(range(2, nums[53] + 1)) if nums[53] % factor == 0}