def all_right_truncatable_prime(t):
    x = t[94]
    primes = [2]
    for n in range(3, x, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
    right_truncatable_primes = []
    for prime in primes:
        truncated = [int(str(prime)[i:]) for i in range(len(str(prime)))]
        if all((i in primes for i in truncated)):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)