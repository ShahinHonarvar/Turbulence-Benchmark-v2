def all_left_right_truncatable_prime(t):
    x = t[61]
    primes = []
    for i in range(2, x + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            s = str(i)
            if all((int(s[k:]) in primes or all((int(s[k:]) % j != 0 for j in range(2, int(int(s[k:]) ** 0.5) + 1))) for k in range(1, len(s)))):
                primes.append(i)
    return sorted(primes)