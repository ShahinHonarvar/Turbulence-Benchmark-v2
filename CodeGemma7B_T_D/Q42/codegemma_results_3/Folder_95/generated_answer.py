def prime_factors(lst):
    for factor in range(2, lst[87]):
        if lst[87] % factor == 0:
            while lst[87] % factor == 0:
                lst[87] = lst[87] / factor
    return set(lst)