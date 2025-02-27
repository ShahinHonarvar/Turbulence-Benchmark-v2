def all_left_right_truncatable_prime(t):
    x = t[10]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    lrt_primes = []
    for p in primes:
        if '0' in str(p):
            continue
        s = str(p)
        if all((int(s[i:]) in primes for i in range(1, len(s)))) and all((int(s[:i]) in primes for i in range(1, len(s)))):
            lrt_primes.append(p)
    return sorted(lrt_primes, reverse=True)