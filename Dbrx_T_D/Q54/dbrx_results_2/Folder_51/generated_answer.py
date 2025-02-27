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

def is_right_truncatable_prime(num):
    while num > 0:
        if num not in primes:
            return False
        num = num // 10
    return True

def all_right_truncatable_prime(tup):
    global primes
    primes = generate_primes(max(tup))
    x = max(tup) + 1
    right_truncatable_primes = []
    for num in range(10, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)