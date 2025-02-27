def prime_factors(nums):
    fourty_eight_factor = set()
    for factor in nums:
        if factor % nums[48] == 0:
            fourty_eight_factor.add(factor)
            while factor % nums[48] == 0:
                factor /= nums[48]
    return forty_eight_factor