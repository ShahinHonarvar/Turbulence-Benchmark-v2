def prime_factors(nums):
    return set((factor for factor in range(2, 994) if all((factor % num != 0 for num in nums))))