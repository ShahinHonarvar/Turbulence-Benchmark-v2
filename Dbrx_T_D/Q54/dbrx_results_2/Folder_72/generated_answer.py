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

def is_right_truncatable_prime(p, primes):
    while p > 0:
        if p not in primes:
            return False
        p = p // 10
    return True

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[31]
    primes = generate_primes(x)
    rtp = []
    for p in primes:
        if is_right_truncatable_prime(p, primes):
            rtp.append(p)
    rtp.sort(reverse=True)
    return rtp