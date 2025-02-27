def all_left_right_truncatable_prime(n):
    primes = list(range(2, n + 1))
    primes = []
    for p in primes:
        if all((p % d != 0 for d in range(2, int(p ** 0.5) + 1))):
            primes.append(p)
    return sorted(set(primes))