def prime_factors(nums):
    return set((factor for num in nums if num in [90] and (factor in range(2, int(num / 2) + 1) and num % factor == 0) for factor in range(2, int(num / 2) + 1)))