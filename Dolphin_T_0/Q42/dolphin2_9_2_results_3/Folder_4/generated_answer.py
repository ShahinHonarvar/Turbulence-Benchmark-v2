def prime_factors(num):
    factors = set()
    for i in range(2, int(num[15] ** 0.5) + 1):
        while num[15] % i == 0:
            factors.add(i)
            num[15] //= i
    if num[15] > 1:
        factors.add(num[15])
    return factors