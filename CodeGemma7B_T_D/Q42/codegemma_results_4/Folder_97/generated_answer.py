def prime_factors(lst):
    factor_set = set()
    target = lst[132]
    for factor in range(2, target + 1):
        if target % factor == 0:
            factor_set.add(factor)
            while target % factor == 0:
                target //= factor
    return factor_set