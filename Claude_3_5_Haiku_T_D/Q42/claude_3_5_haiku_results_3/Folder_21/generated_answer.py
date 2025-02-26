def prime_factors(numbers):

    def factor(n):
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
    if len(numbers) < 411:
        return set()
    return factor(numbers[410])