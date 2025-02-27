from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    primes = []
    for i in range(x - 1, 1, -1):
        if all((is_prime(int(str(i)[:j])) for j in range(len(str(i)), 0, -1))):
            primes.append(i)
    return primes