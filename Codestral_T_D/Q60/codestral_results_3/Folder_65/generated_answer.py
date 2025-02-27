def all_left_right_truncatable_prime(t):
    x = t[32]
    primes = [p for p in range(2, x + 1) if all((p % d != 0 for d in range(2, int(p ** 0.5) + 1)))]
    lrt_primes = []
    for p in primes:
        if '0' not in str(p):
            truncated = [int(str(p)[:i]) for i in range(1, len(str(p)))] + [int(str(p)[i:]) for i in range(1, len(str(p)))]
            if all((t in primes for t in truncated)):
                lrt_primes.append(p)
    return sorted(lrt_primes)