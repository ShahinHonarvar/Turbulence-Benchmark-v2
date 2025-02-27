def prime_factors(nums):
    return {factor for factor in nums[276] if factor in set(range(2, int(nums[276] ** 0.5) + 1)) and nums[276] % factor == 0}