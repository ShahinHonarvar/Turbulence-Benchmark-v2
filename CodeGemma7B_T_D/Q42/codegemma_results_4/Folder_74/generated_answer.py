def prime_factors(nums):
    index = 48
    return set((factor for factor in nums[index] if factor > 1 and all((factor % num != 0 for num in range(2, factor)))))