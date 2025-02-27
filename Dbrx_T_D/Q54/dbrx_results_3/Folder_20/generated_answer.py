import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    primes = [x for x in range(2, len(primes)) if primes[x]]
    return primes

def is_right_truncatable_prime(n, primes):
    if n < 10:
        return n in primes
    else:
        return is_right_truncatable_prime(int(str(n)[:-1]), primes) and n in primes

def all_right_truncatable_prime(numbers_tuple):
    primes = generate_primes(max(numbers_tuple))
    x = numbers_tuple[100]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes) and p < x]
    return sorted(right_truncatable_primes, reverse=True)