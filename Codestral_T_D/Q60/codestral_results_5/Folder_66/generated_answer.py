def all_left_right_truncatable_prime(t):
    x = t[25]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc_prime(n):
        if not is_prime(n):
            return False
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_trunc_prime(i)], reverse=True)