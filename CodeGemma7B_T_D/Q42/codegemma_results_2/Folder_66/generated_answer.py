def prime_factors(l):
    factor_set = set()
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for n in range(14):
        if l[42] % prime_list[n] == 0:
            factor_set.add(prime_list[n])
        if n == 4:
            break
    return factor_set