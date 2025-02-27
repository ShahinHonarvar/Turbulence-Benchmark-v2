def prime_factors(nums):
    factor_set = set()
    target_value = nums[926]
    for num in nums:
        while num % target_value == 0:
            factor_set.add(target_value)
            num //= target_value
    return factor_set