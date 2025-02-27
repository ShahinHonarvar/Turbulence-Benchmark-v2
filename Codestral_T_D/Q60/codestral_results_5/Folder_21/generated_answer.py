def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        while p > 0:
            p = p // 10
            if not is_prime(p):
                return False
        return True

    def is_right_truncatable(p):
        s = str(p)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[175]
    result = []
    for p in range(2, x + 1):
        if '0' not in str(p) and is_prime(p) and is_left_truncatable(p) and is_right_truncatable(p):
            result.append(p)
    return sorted(result)