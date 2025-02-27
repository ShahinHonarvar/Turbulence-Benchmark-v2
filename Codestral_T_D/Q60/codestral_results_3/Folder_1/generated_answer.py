def all_left_right_truncatable_prime(t):
    x = t[20]

    def is_prime(n):
        if n < 2 or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True)