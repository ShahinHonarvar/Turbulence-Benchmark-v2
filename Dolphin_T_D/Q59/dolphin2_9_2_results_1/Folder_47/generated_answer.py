def all_left_truncatable_prime(t):
    primes = []
    x = t[49]
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, i))) and '0' not in str(i):
            for l in range(1, len(str(i))):
                if not all((int(str(i)[l:]) % j != 0 for j in range(2, int(str(i)[l:])))):
                    break
            else:
                primes.append(i)
    return sorted(primes)