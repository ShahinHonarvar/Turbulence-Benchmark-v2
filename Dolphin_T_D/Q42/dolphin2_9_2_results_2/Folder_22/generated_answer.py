def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    return {i for i in prime_factors_iter(lst[72])}

def prime_factors_iter(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            yield i
            if n // i != i:
                yield (n // i)