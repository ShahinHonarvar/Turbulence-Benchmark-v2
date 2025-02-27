def all_left_truncatable_prime(t):
    x = t[39]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
    ltp = []
    for p in primes:
        s = str(p)
        if '0' not in s and all((int(s[i:]) in primes for i in range(1, len(s)))):
            ltp.append(p)
    return sorted(ltp, reverse=True)