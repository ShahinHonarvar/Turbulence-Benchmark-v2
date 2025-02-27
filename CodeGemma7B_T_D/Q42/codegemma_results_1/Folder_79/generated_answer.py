def prime_factors(nums):
    factor_set = set()
    test_num = nums[63]
    for num in range(2, int(test_num ** 0.5) + 1):
        while test_num % num == 0:
            factor_set.add(num)
            test_num //= num
    if test_num > 1:
        factor_set.add(test_num)
    return factor_set