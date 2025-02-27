def all_right_truncatable_prime(t):
    x = t[14]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and all((all((int(i[:k]) % j != 0 for j in range(2, int(int(i[:k]) ** 0.5) + 1))) for k in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)