def all_left_truncatable_prime(t):
    x = t[74]
    primes = [2, 3, 5, 7]
    n = 11
    while n < x:
        if all((n % p != 0 for p in primes)):
            if all((str(n)[i] != '0' for i in range(len(str(n)) - 1))):
                primes.append(n)
        if all((n % p != 0 for p in primes)):
            n += 2
        else:
            n += 1
    return [n for n in primes if n < x]