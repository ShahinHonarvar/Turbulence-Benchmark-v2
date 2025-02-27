def all_right_truncatable_prime(t):
    x = t[77]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    l = sorted(set((i for i in range(1, x) if is_prime(i) and is_right_truncatable(i))))
    return l[::-1] if l else []