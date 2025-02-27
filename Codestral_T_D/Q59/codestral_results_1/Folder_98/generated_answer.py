def all_left_truncatable_prime(t):
    x = t[8]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in primes for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)