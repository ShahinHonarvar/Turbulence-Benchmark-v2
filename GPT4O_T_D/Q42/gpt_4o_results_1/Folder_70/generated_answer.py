def prime_factors(integers):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(integers) > 845:
        return get_prime_factors(integers[845])
    return set()