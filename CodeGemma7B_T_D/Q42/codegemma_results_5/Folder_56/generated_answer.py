from collections import defaultdict

def prime_factors(num):
    if num <= 1:
        return set()
    prime_factors = set()
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            prime_factors.add(factor)
            num //= factor
        else:
            factor += 1
    if num > 1:
        prime_factors.add(num)
    return prime_factors