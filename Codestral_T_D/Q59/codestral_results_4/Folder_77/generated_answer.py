def all_left_truncatable_prime(t):
    x = t[767]
    primes = [p for p in range(2, x) if all((int(str(p)[i:]) in [2, 3, 5, 7] for i in range(len(str(p)))))]
    return sorted(primes, reverse=True)