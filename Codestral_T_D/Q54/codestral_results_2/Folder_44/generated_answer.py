def all_right_truncatable_prime(t):
    x = t[39]
    primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            primes.append(i)
    rtp_primes = []
    for prime in primes:
        num = prime
        while num > 0:
            if num not in primes:
                break
            num //= 10
        else:
            rtp_primes.append(prime)
    return sorted(rtp_primes)