def all_left_truncatable_prime(t):
    x = t[52]
    primes = [2]
    ltp = []
    for i in range(3, x, 2):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    for p in primes:
        num = p
        while num:
            if num not in primes:
                break
            num //= 10
        else:
            ltp.append(p)
    return sorted(ltp, reverse=True)