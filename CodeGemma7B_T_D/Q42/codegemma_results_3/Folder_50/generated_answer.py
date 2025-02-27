def prime_factors(nums):
    return set((factor for factor in range(2, nums[40] + 1) if nums[40] % factor == 0))