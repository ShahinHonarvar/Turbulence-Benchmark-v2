def all_left_truncatable_prime(t):
    x = t[33]
    primes = [2, 3, 5, 7]
    for n in range(10, x):
        if n > 1 and all((n % d != 0 for d in range(2, int(n ** 0.5 + 1)))):
            if all(int((str(n)[i:] for i in range(1, len(str(n))))) in primes):
                primes.append(n)
    return primes[1:]