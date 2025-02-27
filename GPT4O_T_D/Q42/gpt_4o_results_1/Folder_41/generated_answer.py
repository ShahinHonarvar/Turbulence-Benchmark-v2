def prime_factors(integers):

    def get_prime_factors(n):
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
    if len(integers) > 84:
        return get_prime_factors(integers[84])
    return set()