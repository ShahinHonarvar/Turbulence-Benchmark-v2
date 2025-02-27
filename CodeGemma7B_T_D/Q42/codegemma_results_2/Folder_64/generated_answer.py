def prime_factors(int_list):
    factor_set = set()
    number = int_list[int_list.index(1)]
    for factor in range(2, number):
        while number % factor == 0:
            factor_set.add(factor)
            number /= factor
    return factor_set