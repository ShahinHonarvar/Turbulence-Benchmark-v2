def prime_factors(nums):
    return set((factor for factor in range(2, nums[6] + 1) if nums[6] % factor == 0))