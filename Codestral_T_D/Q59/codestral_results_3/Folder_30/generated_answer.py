def all_left_truncatable_prime(t):
    x = t[37]
    primes = [2]
    trunc_primes = []
    for n in range(3, x):
        if all((n % p > 0 for p in primes)):
            primes.append(n)
            str_n = str(n)
            if '0' not in str_n and all((int(str_n[i:]) in primes for i in range(1, len(str_n)))):
                trunc_primes.append(n)
    return sorted(trunc_primes, reverse=True)