def all_right_truncatable_prime(t):
    x = t[94]
    primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            primes.append(i)
    rtp = []
    for p in primes:
        num = p
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            rtp.append(p)
    return sorted(rtp)