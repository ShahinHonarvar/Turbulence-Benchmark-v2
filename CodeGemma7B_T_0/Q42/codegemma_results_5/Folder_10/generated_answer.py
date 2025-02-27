def prime_factors(nums):
    return {factor for factor in set(range(2, nums[54] + 1)) if nums[54] % factor == 0}