from math import sqrt

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for i in range(2, x):
        if all((isprime(i // 10 ** (len(str(i)) - j)) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes)