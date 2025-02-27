def prime_factors(nums):
    return set((factor for factor in nums[321] if all((num % factor != 0 for num in nums))))