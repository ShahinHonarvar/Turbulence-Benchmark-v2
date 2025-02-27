import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[618]
    primes = []
    for n in range(2, x):
        n_str = str(n)
        while len(n_str) > 0:
            if not is_prime(int(n_str)):
                break
            if len(n_str) == 1:
                primes.append(n)
                break
            n_str = n_str[:-1]
    primes = list(set(primes))
    primes.sort()
    return primes