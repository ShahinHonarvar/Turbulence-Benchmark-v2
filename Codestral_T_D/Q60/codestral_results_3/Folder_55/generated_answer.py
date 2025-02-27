def all_left_right_truncatable_prime(t):
    x = t[73]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if s[i] == '0':
                return False
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)], reverse=True)