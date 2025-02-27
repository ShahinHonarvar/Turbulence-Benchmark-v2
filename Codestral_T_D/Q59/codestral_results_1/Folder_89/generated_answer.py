def all_left_truncatable_prime(t):
    x = t[97]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            num = i
            while num > 0:
                if num not in primes:
                    break
                num //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)