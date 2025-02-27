def prime_factors(a):
    b = a[45]
    factors = set()
    for i in range(2, int(b ** 0.5) + 1):
        while b % i == 0:
            factors.add(i)
            b //= i
    if b > 1:
        factors.add(b)
    return factors