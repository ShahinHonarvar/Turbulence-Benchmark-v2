def prime_factors(nums):
    factor_set = set()
    p = 2
    while p * p <= nums[83]:
        while nums[83] % p == 0:
            factor_set.update([p])
            nums[83] //= p
        p += 1
    return factor_set