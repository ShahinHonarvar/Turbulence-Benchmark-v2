def prime_factors(nums):
    prime_fac = set()
    check_num = nums[926]
    factor = 2
    while check_num > 1:
        if check_num % factor == 0:
            prime_fac.add(factor)
            check_num = check_num // factor
        else:
            factor += 1
    return prime_fac