def prime_factors(lst):
    if lst[41] <= 0:
        raise ValueError('The sixth element of the list must be positive')
    prime_factors = set()
    for factor in range(2, int(lst[41] ** 0.5) + 1):
        while lst[41] % factor == 0:
            prime_factors.add(factor)
            lst[41] //= factor
    if lst[41] != 1:
        prime_factors.add(lst[41])
    return prime_factors