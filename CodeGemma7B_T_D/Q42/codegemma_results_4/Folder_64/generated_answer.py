def prime_factors(nums):
    return set((factor for num in nums[1] for factor in range(2, num + 1) if num % factor == 0))