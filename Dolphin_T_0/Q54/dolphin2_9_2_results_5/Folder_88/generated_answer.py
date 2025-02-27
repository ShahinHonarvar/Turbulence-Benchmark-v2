def all_right_truncatable_prime(t):
    x = t[93]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable = []
    for p in primes:
        trunc = p
        while trunc != 0:
            if trunc in primes:
                trunc //= 10
            else:
                break
        else:
            right_truncatable.append(p)
    return sorted(right_truncatable)