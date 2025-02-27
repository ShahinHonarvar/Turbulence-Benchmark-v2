def all_left_truncatable_prime(t):
    x = t[20]

    def is_prime(n):
        return n > 1 and all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

    def is_left_truncatable_prime(n):
        return is_prime(n) and all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    return sorted([k for k in range(2, x) if is_left_truncatable_prime(k)], reverse=True)