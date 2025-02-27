def all_left_truncatable_prime(tup):
    x = tup[19]

    def is_prime(n):
        return n > 1 and all((n % d != 0 for d in range(2, int(n ** 0.5) + 1)))

    def is_truncatable(n):
        return '0' not in str(n) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))))
    return sorted([k for k in range(x) if is_prime(k) and is_truncatable(k)])