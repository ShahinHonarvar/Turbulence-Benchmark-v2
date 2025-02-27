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
    if num < 10:
        return True
    for i in range(1, len(str(num)) + 1):
        if not is_prime(int(str(num)[:-i])):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(range_tuple):
    x = range_tuple[18]
    primes = [p for p in generate_primes(x) if is_right_truncatable_prime(p)]
    return sorted(primes, reverse=True)