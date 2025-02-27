def prime_factors(int_list):
    pf = set()
    for factor in range(2, int_list[162] + 1):
        while int_list[162] % factor == 0:
            pf.add(factor)
            int_list[162] //= factor
    return pf