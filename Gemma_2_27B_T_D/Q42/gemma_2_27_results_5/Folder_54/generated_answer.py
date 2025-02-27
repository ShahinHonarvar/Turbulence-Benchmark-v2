def prime_factors(lst):
    n = lst[51]
    i = 2
    factors = set()
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return factors