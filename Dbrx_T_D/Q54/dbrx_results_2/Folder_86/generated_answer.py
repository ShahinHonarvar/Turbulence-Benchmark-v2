def generate_primes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0], primes[1] = (False, False)
    prime_numbers = [i for i, prime in enumerate(primes) if prime]
    return prime_numbers

def is_right_truncatable_prime(n, primes):
    if n < 10:
        return True
    while n > 0:
        if n not in primes:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(t):
    primes = generate_primes(max(t))
    x = t[126]
    right_truncatable_primes = []
    for prime in primes:
        if prime >= x:
            break
        if is_right_truncatable_prime(prime, primes):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)