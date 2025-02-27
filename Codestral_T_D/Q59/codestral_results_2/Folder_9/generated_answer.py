def all_left_truncatable_prime(t):
    x = t[29]
    primes = [i for i in range(2, x) if all((j != 0 and all((int(str(j)[:i]) in primes for i in range(1, len(str(j))))) for j in range(2, int(str(x)[:i])))) for i in range(1, len(str(x)))]
    return sorted(primes, reverse=True)