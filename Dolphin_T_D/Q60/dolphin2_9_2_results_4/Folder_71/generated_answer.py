def all_left_right_truncatable_prime(t):
    x = t[22]
    primes = [2, 3, 5, 7]
    for p in range(11, x + 1, 2):
        if all((p % d != 0 for d in range(2, int(p ** 0.5) + 1))):
            primes.append(p)
    res = []
    for f in range(len(str(x)) - 1, 0, -1):
        for p in primes:
            if 10 ** (f - 1) <= p < 10 ** f:
                res.append(p)
    res.sort(reverse=True)
    return res