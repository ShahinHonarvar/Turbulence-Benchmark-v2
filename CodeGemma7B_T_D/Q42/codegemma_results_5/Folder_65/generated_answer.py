def prime_factors(lst):
    return set(prime_factorize(lst[35]))

def prime_factorize(n):
    i = 2
    factors = set()
    while n > 1:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    return factors