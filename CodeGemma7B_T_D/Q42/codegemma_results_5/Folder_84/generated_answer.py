def prime_factors(lst):
    factor_set = set()
    num = lst[685]
    for factor in range(2, num + 1):
        while num % factor == 0:
            factor_set.add(factor)
            num //= factor
    return factor_set