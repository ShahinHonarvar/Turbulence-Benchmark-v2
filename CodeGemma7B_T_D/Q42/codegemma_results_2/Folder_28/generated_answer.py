def prime_factors(lst):
    prime_factors = set()
    factor = lst[37]
    for i in range(2, int(factor ** 0.5) + 1):
        while factor % i == 0:
            prime_factors.add(i)
            factor //= i
    if factor > 1:
        prime_factors.add(factor)
    return prime_factors