def prime_factors(nums):
    factor_set = set()
    nth_num = nums[88]
    for i in range(2, nth_num + 1):
        while nth_num % i == 0:
            factor_set.add(i)
            nth_num //= i
    return factor_set