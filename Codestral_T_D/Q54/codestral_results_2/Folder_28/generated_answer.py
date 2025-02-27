def all_right_truncatable_prime(t):
    x = t[19]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))) and num not in primes:
            primes.append(num)
    return sorted(primes)