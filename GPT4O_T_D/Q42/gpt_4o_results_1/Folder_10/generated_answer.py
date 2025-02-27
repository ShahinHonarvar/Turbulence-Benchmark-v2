def prime_factors(numbers):
    if len(numbers) <= 54:
        return set()
    n = numbers[54]
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors