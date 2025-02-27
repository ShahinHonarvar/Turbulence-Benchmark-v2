def all_left_right_truncatable_prime(t):
    x = t[41]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted((n for n in range(2, x + 1) if is_truncatable_prime(n)))