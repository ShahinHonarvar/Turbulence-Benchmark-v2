def prime_factors(nums):
    prime_factors_478 = set()
    for factor in nums:
        if factor % nums[478] == 0 and factor != nums[478]:
            prime_factors_478.add(factor)
    return prime_factors_478