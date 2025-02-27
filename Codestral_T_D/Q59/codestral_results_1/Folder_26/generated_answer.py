def all_left_truncatable_prime(t):
    x = t[81]
    primes = [2]
    ltrp_primes = []
    for i in range(3, x):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            if '0' not in str(i):
                truncated = set((int(str(i)[j:]) for j in range(1, len(str(i)))))
                if truncated.issubset(primes):
                    ltrp_primes.append(i)
    return sorted(ltrp_primes, reverse=True)