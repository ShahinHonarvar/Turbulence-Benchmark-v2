def all_left_right_truncatable_prime(t):
    x = t[23]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))

    def is_right_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_left_truncatable(n) and is_right_truncatable(n)])