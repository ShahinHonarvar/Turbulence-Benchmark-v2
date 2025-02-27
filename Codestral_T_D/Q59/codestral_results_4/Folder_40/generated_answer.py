def all_left_truncatable_prime(t):
    x = t[10]
    primes = [2] + [i for i in range(3, x, 2) if all((i % j != 0 for j in range(3, int(i ** 0.5) + 1, 2)))]
    ltp_primes = sorted([p for p in primes if all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))], reverse=True)
    return ltp_primes