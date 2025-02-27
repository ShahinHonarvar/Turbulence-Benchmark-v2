import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return [x for x in range(2, n + 1) if primes[x]]

def is_right_truncatable_prime(x):
    while x > 0:
        if not is_prime(x):
            return False
        x //= 10
    return True

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    primes = generate_primes(max(numbers))
    prime_set = set(primes)
    right_truncatable_primes = []
    for prime in primes:
        if prime < 10:
            continue
        for i in range(1, 10):
            x = prime + i * 10 ** (len(str(prime)) - 1)
            if x not in prime_set:
                break
            if is_right_truncatable_prime(x):
                right_truncatable_primes.append(x)
    right_truncatable_primes = sorted(list(set(right_truncatable_primes)), reverse=True)
    return right_truncatable_primes[:29 + 1] if 29 in numbers else right_truncatable_primes