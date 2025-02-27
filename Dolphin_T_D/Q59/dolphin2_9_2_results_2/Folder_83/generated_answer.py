def all_left_truncatable_prime(x):
    primes = [2]
    i = 3
    while i < x:
        if all((i % p != 0 for p in primes)):
            primes.append(i)
        i += 2
    left_truncatable_primes = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(1, len(str(p))))) and p < x]
    return sorted(left_truncatable_primes)