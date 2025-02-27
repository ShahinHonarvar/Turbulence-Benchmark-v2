def prime_factors(lst):
    factor_set = set()
    value = lst[746]
    for factor in range(2, int(value ** 0.5) + 1):
        while value % factor == 0:
            factor_set.add(factor)
            value //= factor
    if value > 1:
        factor_set.add(value)
    return factor_set