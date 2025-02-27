import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] == '0':
            return False
        n1 = int(n_str[i + 1:])
        if not is_prime(n1):
            return False
        n2 = int(n_str[:-i - 1])
        if not is_prime(n2):
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)