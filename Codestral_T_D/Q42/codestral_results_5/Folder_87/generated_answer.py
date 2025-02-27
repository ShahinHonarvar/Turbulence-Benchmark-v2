def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            factors.add(n)
        return factors
    return get_prime_factors(numbers[96])