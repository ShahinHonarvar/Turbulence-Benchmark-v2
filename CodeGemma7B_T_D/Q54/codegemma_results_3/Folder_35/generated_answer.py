def all_right_truncatable_prime(t):
    x = t[177]
    primes = []
    for n in range(2, x):
        if all([n % d != 0 for d in range(2, int(n ** 0.5) + 1)]):
            k = n
            while k > 0 and all([k % d != 0 for d in range(2, int(k ** 0.5) + 1)]):
                k //= 10
                primes.append(n)
    return sorted(primes)