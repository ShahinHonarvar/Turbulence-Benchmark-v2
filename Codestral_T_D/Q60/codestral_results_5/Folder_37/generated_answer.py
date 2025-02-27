def all_left_right_truncatable_prime(t):
    x = t[35]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i)]
    lr_primes = []
    for p in primes:
        if all((int(str(p)[:i]) in primes and int(str(p)[i:]) in primes for i in range(1, len(str(p))))):
            lr_primes.append(p)
    return sorted(lr_primes, reverse=True)