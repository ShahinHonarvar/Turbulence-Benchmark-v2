def all_left_truncatable_prime(t):
    x = t[88]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    return [p for p in primes if all((int(str(p)[j:]) in primes for j in range(1, len(str(p)))))]