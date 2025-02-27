def all_right_truncatable_prime(t):
    x = t[38]
    truncate = set((str(i) for i in range(2, x) if all((int(str(i)[:-j]) in primes for j in range(1, len(str(i)))))))
    truncate.discard(2)
    return sorted(truncate, reverse=True)