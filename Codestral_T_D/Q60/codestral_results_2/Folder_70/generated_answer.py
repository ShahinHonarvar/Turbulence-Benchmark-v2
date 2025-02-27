def all_left_right_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i)]
    trunc_primes = []
    for p in primes:
        s = str(p)
        if all((int(s[i:]) in primes and int(s[:i]) in primes for i in range(1, len(s)))):
            trunc_primes.append(p)
    return sorted(trunc_primes, reverse=True)