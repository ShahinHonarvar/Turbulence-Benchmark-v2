import itertools

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    for p in range(int(n ** 0.5) + 1, n + 1):
        if sieve[p]:
            primes.append(p)
    return primes

def is_right_truncatable_prime(p):
    while p > 0:
        if p not in primes:
            return False
        p = int(str(p)[1:])
    return True

def all_right_truncatable_prime(t):
    global primes
    primes = generate_primes(t[77])
    rtp = [p for p in primes if is_right_truncatable_prime(p)]
    rtp.sort(reverse=True)
    return rtp