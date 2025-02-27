def prime_factors(lst):
    return set(prime_factorize(lst[17]))

def prime_factorize(n):
    factors = set()
    d = 2
    while n > 1:
        if n % d == 0:
            factors.add(d)
            n /= d
        else:
            d += 1
    return factors