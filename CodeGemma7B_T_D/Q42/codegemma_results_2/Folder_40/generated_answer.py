def prime_factors(lst):
    factor_set = set()
    for factor in lst[7]:
        if factor % 2 == 0:
            factor_set.add(2)
            while factor % 5 == 0:
                factor = factor // 5
        elif factor % 3 == 0:
            factor_set.add(3)
            while factor % 3 == 0:
                factor = factor // 3
        elif factor % 5 == 0:
            factor_set.add(5)
            while factor % 5 == 0:
                factor = factor // 5
        elif factor % 7 == 0:
            factor_set.add(7)
            while factor % 7 == 0:
                factor = factor // 7
        else:
            factor_set.add(factor)
    return factor_set