def prime_factors(nums):
    return set((factor for num in nums[20] for factor in range(2, num) if num % factor == 0))