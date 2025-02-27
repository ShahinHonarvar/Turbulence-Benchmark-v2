def all_left_right_truncatable_prime(t):
    x = t[767]
    primes = [2, 3, 5, 7]
    others = [1, 4, 6, 8, 9]
    for i in range(3, int(x ** 0.5) + 1, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            if i >= 10:
                for j in range(len(others)):
                    n = 10 * i + others[j]
                    if n < x and all((n % p != 0 for p in primes)):
                        primes.append(n)
    return [p for p in sorted(primes, reverse=True) if p <= x]