def all_right_truncatable_prime(t):

    def is_right_truncatable(n):
        if n < 10:
            return primes[n]
        else:
            return is_right_truncatable(n // 10) and primes[n]
    n = t[28]
    primes = [False, False] + [True] * (n - 2)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return sorted([i for i, prime in enumerate(primes) if prime and is_right_truncatable(i)])