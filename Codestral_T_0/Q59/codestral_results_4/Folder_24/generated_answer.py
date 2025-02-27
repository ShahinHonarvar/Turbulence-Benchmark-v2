def all_left_truncatable_prime(t):
    x = t[65]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
    ltp_primes = []
    for p in primes:
        num = p
        while num:
            if num not in primes:
                break
            num //= 10
        else:
            ltp_primes.append(p)
    return sorted(ltp_primes, reverse=True)