def all_right_truncatable_prime(t):
    x = t[618]
    primes = []
    for possible in range(2, x):
        if all((possible % i != 0 for i in range(2, int(possible ** 0.5) + 1))):
            if all((int(str(possible)[:i]) in primes for i in range(1, len(str(possible))))):
                primes.append(possible)
    return sorted(primes)