def prime_factors(nums):
    return {factor for factor in set(range(2, nums[97] + 1)) if nums[97] % factor == 0}