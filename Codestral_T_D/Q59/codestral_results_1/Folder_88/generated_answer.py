def all_left_truncatable_prime(t):
    x = t[93]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    lt_primes = []
    for prime in primes:
        num = prime
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            lt_primes.append(prime)
    return sorted(lt_primes)