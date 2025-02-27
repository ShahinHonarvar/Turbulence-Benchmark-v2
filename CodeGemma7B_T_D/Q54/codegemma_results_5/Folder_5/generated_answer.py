def all_right_truncatable_prime(t):
    x = t[55]
    all_primes = [i for i in range(2, x) if all((i % j for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for p in all_primes:
        for i in range(1, len(str(p))):
            if p % int(str(p)[:-i]) != 0:
                break
        else:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes) if right_truncatable_primes else []