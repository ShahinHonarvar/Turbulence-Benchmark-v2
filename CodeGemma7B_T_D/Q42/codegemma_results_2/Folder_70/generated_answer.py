def prime_factors(nums):
    factor_set = set()
    target_num = nums[845]
    for num in range(2, int(target_num ** 0.5) + 1):
        while target_num % num == 0:
            factor_set.add(num)
            target_num //= num
    factor_set.add(target_num)
    return factor_set