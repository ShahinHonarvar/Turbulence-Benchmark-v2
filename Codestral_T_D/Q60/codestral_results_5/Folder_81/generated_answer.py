def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if '0' in s[i:] or '0' in s[:i + 1]:
                return False
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
                return False
        return True
    x = t[98]
    return sorted([n for n in range(2, x + 1) if truncatable(n)])