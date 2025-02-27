import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0:2] = [False, False]
    return [p for p in range(n + 1) if primes[p]]

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_right_truncatable_prime(tuples):
    x = tuples[73]
    primes = generate_primes(x - 1)
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)