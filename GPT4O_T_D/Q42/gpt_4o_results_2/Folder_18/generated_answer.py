def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= divisor * divisor:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(lst) > 312:
        return get_prime_factors(lst[312])
    return set()