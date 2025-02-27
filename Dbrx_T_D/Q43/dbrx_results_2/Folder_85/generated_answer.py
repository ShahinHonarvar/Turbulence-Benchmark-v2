from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in lst[32:36]:
        if is_prime(i):
            primes.append(i)
    primes.sort()
    return primes