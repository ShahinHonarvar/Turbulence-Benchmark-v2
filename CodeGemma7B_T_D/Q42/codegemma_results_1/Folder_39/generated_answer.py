def prime_factors(lst):
    factors = set()
    for factor in range(2, lst[59] + 1):
        while lst[59] % factor == 0:
            factors.add(factor)
            lst[59] //= factor
    return factors