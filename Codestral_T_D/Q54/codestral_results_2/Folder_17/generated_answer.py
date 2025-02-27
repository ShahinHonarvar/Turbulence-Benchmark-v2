def all_right_truncatable_prime(tup):
    x = tup[36]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = [p for p in primes if all((int(str(p)[:i]) in primes for i in range(1, len(str(p)))))]
    return sorted(right_truncatable_primes, reverse=True)