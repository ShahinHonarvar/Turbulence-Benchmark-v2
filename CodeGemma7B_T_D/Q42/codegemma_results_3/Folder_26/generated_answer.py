def prime_factors(nums):
    factor_set = set()
    target = nums[222]
    for num in range(2, target + 1):
        while target % num == 0:
            factor_set.add(num)
            target //= num
    return factor_set