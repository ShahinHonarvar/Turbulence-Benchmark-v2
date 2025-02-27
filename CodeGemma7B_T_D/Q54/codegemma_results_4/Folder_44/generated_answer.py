def all_right_truncatable_prime(tu):
    x = tu[39]
    primes = [q for q in range(2, x) if all((q % k != 0 for k in range(2, int(q ** 0.5) + 1)))]
    right_truncatable_primes = []
    for p in primes:
        right_truncatable = True
        q = p
        while q > 0:
            if q not in primes:
                right_truncatable = False
                break
            q //= 10
        if right_truncatable:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes) if right_truncatable_primes else []