def all_left_truncatable_prime(t):
    x = t[31]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    ltp_primes = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    return sorted(ltp_primes, reverse=True)