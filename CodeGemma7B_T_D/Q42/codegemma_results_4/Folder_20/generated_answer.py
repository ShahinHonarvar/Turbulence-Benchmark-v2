def prime_factors(nums):
    return set((factor for factor in range(2, nums[53] + 1) if nums[53] % factor == 0))