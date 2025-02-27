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
    n = str(n)
    if int(n) <= 1:
        return False
    for i in range(1, len(n)):
        if int(n[i:]) not in prime_numbers:
            return False
    return True

def all_left_truncatable_prime(n):
    return sorted([p for p in prime_numbers if is_left_truncatable_prime(p) and p < n[23]])