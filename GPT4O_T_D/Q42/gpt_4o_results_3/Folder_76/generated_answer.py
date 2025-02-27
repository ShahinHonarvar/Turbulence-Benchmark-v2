def prime_factors(integers):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if 537 < len(integers):
        return get_prime_factors(integers[537])
    return set()