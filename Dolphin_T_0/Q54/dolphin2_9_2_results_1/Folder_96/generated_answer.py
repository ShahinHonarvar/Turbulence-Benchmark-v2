def all_right_truncatable_prime(t):
    x = t[29]
    primes = [2, 3, 5, 7]
    for p in primes:
        while True:
            if len(str(p)) == 1:
                break
            p = int(str(p)[-1])
            if p in primes:
                primes.append(p)
    return sorted([p for p in primes if p < x])