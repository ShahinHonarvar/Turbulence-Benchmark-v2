def prime_factors(nums):
    prime_factors_set = set()
    for factor in nums:
        if factor % nums[83] == 0 and factor != nums[83]:
            prime_factors_set.add(factor)
    return prime_factors_set