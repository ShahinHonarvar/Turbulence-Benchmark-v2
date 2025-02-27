def all_right_truncatable_prime(t):
    x = t[175]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, i))):
            trunc = str(i)
            while len(trunc) > 1:
                if not all((int(trunc[:-j]) % j != 0 for j in range(1, len(trunc)))):
                    break
                trunc = trunc[:-1]
            else:
                primes.append(i)
    return sorted(primes)