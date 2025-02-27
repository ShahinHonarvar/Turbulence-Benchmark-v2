import itertools

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False
    primes.extend((i for i in range(int(n ** 0.5) + 1, n + 1) if sieve[i]))
    return primes

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(t):
    primes = generate_primes(t[32])
    return sorted(filter(is_left_truncatable_prime, primes))