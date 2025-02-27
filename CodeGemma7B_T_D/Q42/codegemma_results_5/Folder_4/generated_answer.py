def prime_factors(nums):
    return set([n for n in range(2, nums[15] + 1) if nums[15] % n == 0])