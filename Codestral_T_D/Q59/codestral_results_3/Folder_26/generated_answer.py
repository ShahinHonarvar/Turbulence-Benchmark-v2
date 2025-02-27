def all_left_truncatable_prime(t):
    x = t[80]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            if all((int(str(i)[k:]) in primes for k in range(1, len(str(i))))):
                primes.append(i)
    return sorted(primes, reverse=True)