def all_left_right_truncatable_prime(t):
    x = t[81]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    trunc_primes = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            left_trunc = [int(str_p[i:]) for i in range(1, len(str_p))]
            right_trunc = [int(str_p[:i]) for i in range(1, len(str_p))]
            if all((t in primes for t in left_trunc)) and all((t in primes for t in right_trunc)):
                trunc_primes.append(p)
    return sorted(trunc_primes, reverse=True)