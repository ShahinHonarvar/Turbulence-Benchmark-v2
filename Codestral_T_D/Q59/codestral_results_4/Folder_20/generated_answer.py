def all_left_truncatable_prime(t):
    x = t[100]
    sieve = [True] * x
    for x in range(2, int(x ** 0.5) + 1):
        if sieve[x]:
            for i in range(x * x, x, -x):
                sieve[i] = False
    primes = [i for i in range(2, x) if sieve[i]]
    lt_primes = []
    for p in primes:
        if all((int(str(p)[i:]) in primes for i in range(1, len(str(p))))):
            lt_primes.append(p)
    return sorted(lt_primes, reverse=True)