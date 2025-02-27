def all_left_truncatable_prime(t):
    x = t[6]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    left_truncatable_primes = []
    for p in primes:
        num = p
        while num:
            if num not in primes:
                break
            num //= 10
        else:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)