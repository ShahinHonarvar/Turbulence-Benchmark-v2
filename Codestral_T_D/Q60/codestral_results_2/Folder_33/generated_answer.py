def all_left_right_truncatable_prime(t):
    x = t[945]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncated_prime(n):
        while n > 0:
            if n < 10:
                return False
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncated_prime(n):
        s = str(n)
        while s:
            if '0' in s:
                return False
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True

    def is_left_right_truncated_prime(n):
        return is_left_truncated_prime(n) and is_right_truncated_prime(n)
    return sorted([n for n in range(2, x + 1) if '0' not in str(n) and is_left_right_truncated_prime(n)], reverse=True)