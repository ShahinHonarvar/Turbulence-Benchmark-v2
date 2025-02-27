def all_left_truncatable_prime(t):
    x = t[36]
    primes = []
    for n in range(2, x):
        if all((int(str(n)[:i]) in primes for i in range(1, len(str(n))))) and all((n % j > 0 for j in range(2, int(n ** 0.5) + 1))) and ('0' not in str(n)):
            primes.append(n)
    return sorted(primes)