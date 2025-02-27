def all_left_truncatable_prime(t):
    x = t[1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    return sorted([n for n in range(x) if is_left_truncatable(n)], reverse=True)