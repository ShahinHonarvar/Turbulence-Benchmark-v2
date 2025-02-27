from math import sqrt

def prime_factors(lst):
    prime_factors = set()
    n = lst[94]
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            prime_factors.add(i)
            n //= i
    if n > 1:
        prime_factors.add(n)
    return prime_factors