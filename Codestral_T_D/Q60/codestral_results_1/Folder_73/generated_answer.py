def all_left_right_truncatable_prime(t):
    x = t[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:-i - 1]))):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)])