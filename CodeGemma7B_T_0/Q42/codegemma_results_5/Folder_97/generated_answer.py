def prime_factors(nums):
    return set((factor for num in nums for factor in get_prime_factors(num) if num == nums[132]))