def all_left_truncatable_prime(t):
    x = t[97]
    primes = []
    for p in range(2, x):
        if all((int(str(p)[i:]) in primes for i in range(1, len(str(p))))):
            primes.append(p)
    return sorted(primes, reverse=True)