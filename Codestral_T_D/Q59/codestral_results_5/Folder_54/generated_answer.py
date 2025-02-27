def all_left_truncatable_prime(t):
    x = t[88]
    primes = [2]
    trunc_primes = []
    for i in range(3, x, 2):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    for prime in primes:
        num = prime
        while num:
            if num not in primes:
                break
            num //= 10
        else:
            trunc_primes.append(prime)
    return sorted(trunc_primes, reverse=True)