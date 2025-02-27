import itertools

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False
    primes.extend([num for num in range(int(n ** 0.5) + 1, n + 1) if sieve[num]])
    return primes

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n = int(str(n)[1:])
    return True

def all_right_truncatable_prime(t):
    primes = generate_primes(max(t))
    x = t[84]
    rtp = [num for num in primes if is_right_truncatable_prime(num, primes) and num < x]
    return sorted(rtp)