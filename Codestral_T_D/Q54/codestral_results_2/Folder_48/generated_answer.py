def all_right_truncatable_prime(t):
    x = t[835]
    primes = [2]
    truncatable_primes = []
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            truncated = [int(str(i)[:j]) for j in range(1, len(str(i)))]
            if all((t in primes for t in truncated)):
                truncatable_primes.append(i)
    return sorted(truncatable_primes)