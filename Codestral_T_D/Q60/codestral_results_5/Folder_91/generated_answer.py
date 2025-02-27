def all_left_right_truncatable_prime(t):
    x = t[0]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted([n for n in range(2, x + 1) if '0' not in str(n) and is_prime(n) and is_truncatable(n)], reverse=True)