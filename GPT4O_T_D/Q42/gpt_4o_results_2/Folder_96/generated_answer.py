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
    if len(integers) <= 47:
        return set()
    return get_prime_factors(integers[47])