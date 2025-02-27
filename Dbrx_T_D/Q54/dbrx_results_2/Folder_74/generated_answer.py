import itertools

def generate_primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False
    for num in range(int(n ** 0.5) + 1, n + 1):
        if sieve[num]:
            primes.append(num)
    return primes

def is_right_truncatable_prime(n, primes):
    while n:
        if n not in primes:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(t):
    x = t[36]
    primes = generate_primes(x)
    right_truncatable_primes = []
    for num in itertools.count():
        if num not in primes:
            break
        if is_right_truncatable_prime(num, primes):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)