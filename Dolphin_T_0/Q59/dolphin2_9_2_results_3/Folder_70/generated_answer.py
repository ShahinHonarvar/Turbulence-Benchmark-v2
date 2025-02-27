import math

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[433]
    lt_primes = [2]
    for i in range(3, x + 1):
        if '0' not in str(i) and all((is_prime(int(i[j:])) for j in range(len(str(i)) - 1, 0, -1))):
            lt_primes.append(i)
    lt_primes.sort(reverse=True)
    return lt_primes