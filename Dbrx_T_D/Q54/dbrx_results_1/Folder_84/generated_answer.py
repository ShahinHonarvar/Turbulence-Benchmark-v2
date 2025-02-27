import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    prime_list = []
    for i in range(2, n + 1):
        if primes[i]:
            prime_list.append(i)
    return prime_list

def is_right_truncatable_prime(prime, primes):
    while prime > 0:
        if prime not in primes:
            return False
        prime = prime // 10
    return True

def all_right_truncatable_prime(t):
    primes = generate_primes(10 ** 7)
    x = sorted(list(t[630]))
    x = int(''.join((str(i) for i in x)))
    rtp = [i for i in primes if is_right_truncatable_prime(i, primes) and i < x]
    if not rtp:
        return []
    return sorted(rtp, reverse=True)