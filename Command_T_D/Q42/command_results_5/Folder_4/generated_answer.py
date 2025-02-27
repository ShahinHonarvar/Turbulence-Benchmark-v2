def prime_factors(nums):
    factors = set()
    for num in nums:
        if num > 1:
            factors.update(nums[num:])
    return factors