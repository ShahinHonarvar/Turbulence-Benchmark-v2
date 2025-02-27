def all_left_right_truncatable_prime(t):
    x = t[0]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            s = s[1:]
            if not is_prime(int(s)):
                return False
            s = s[:-1]
            if not is_prime(int(s)):
                return False
        return True
    res = []
    for i in range(x, 1, -1):
        if is_truncatable(i):
            res.append(i)
    return res