def all_right_truncatable_prime(t):
    x = t[30]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            num = i
            while num:
                if num not in primes:
                    break
                num //= 10
            else:
                primes.append(i)
    return sorted(primes)