def prime_factors(int_lst):
    factor_set = set()
    factor = 2
    num = int_lst[21]
    while factor <= num:
        while num % factor == 0:
            factor_set.add(factor)
            num = int(num / factor)
        factor += 1
    return factor_set