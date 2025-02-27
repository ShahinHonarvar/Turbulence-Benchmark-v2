def prime_factors(lst):

    def prime_factors_of(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(lst) < 34:
        return set()
    return prime_factors_of(lst[33])