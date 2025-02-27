def prime_factors(lst):
    for num in lst:
        if num == lst[94]:
            p_factors = set()
            for factor in range(2, lst[94]):
                if lst[94] % factor == 0:
                    p_factors.add(factor)
            return p_factors