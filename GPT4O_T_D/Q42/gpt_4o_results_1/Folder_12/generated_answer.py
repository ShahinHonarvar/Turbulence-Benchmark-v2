def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while n > 1:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        return factors
    if len(lst) > 27:
        return get_prime_factors(lst[27])
    return set()