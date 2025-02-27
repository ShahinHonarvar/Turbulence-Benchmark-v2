import math

def prime_factors(lst):

    def prime_factors_n(n):
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
    if len(lst) > 33:
        return prime_factors_n(lst[33])
    else:
        return 'The list is too short. It must contain at least 34 elements.'