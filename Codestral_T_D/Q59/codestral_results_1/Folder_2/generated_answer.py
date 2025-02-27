def all_left_truncatable_prime(t):
    x = t[618]
    primes = []
    for n in range(2, x):
        if all((int(str(n)[i:]) in primes for i in range(1, len(str(n))))):
            primes.append(n)
    return sorted(primes)