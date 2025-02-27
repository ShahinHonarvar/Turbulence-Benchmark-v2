def prime_factors(lst):
    factor_set = set()
    for num in lst:
        if num != lst[45]:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    factor_set.add(factor)
    for factor in range(2, int(lst[45] ** 0.5) + 1):
        if lst[45] % factor == 0:
            factor_set.add(factor)
            factor_set.add(lst[45] // factor)
    return factor_set