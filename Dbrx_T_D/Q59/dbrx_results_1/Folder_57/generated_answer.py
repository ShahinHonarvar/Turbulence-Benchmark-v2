import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [x for x in range(2, len(primes)) if primes[x]]
    return prime_numbers

def is_left_truncatable_prime(n):
    if n < 10:
        return n in {2, 3, 5, 7}
    return is_left_truncatable_prime(n // 10) and n % 10 != 0 and (n in primes)

def all_left_truncatable_prime(t):
    primes = generate_primes(t[53])
    result = []
    for p in primes:
        if is_left_truncatable_prime(p):
            result.append(p)
    return sorted(result, reverse=True)