import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    return [i for i in range(1, n) if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]

def all_left_truncatable_prime(t):
    x = t[14]
    return sorted(left_truncatable_primes(x), reverse=True)