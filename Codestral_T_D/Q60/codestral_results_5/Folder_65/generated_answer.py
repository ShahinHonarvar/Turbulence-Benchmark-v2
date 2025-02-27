def all_left_right_truncatable_prime(t):
    x = t[32]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    lrt_primes = [p for p in primes if '0' not in str(p) and all((int(str(p)[i:]) in primes and int(str(p)[:-i]) in primes for i in range(1, len(str(p)))))]
    return sorted(lrt_primes)