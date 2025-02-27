def all_left_truncatable_prime(t):
    x = t[89]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p > 0 for p in primes)):
            primes.append(i)
    left_truncatable_primes = [p for p in primes if not '0' in str(p) and all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    return sorted(left_truncatable_primes, reverse=True)