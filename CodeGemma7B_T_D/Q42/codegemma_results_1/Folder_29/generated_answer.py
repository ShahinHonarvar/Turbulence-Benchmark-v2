def prime_factors(lst):
    i = 19
    prime_factors = set()
    factor = lst[i]
    for j in range(2, int(factor ** 0.5) + 1):
        while factor % j == 0:
            prime_factors.add(j)
            factor //= j
    if factor != 1:
        prime_factors.add(factor)
    return prime_factors