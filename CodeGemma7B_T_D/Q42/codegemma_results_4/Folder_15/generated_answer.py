def prime_factors(nums):
    return {factor for factor in range(2, int(nums[10] ** 0.5) + 1) if nums[10] % factor == 0} | {nums[10]}