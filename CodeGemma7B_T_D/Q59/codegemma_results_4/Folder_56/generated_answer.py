def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    l, u = t
    l = max(l, 2)
    res = []
    for i in range(l, u):
        if is_prime(i) and is_left_truncatable_prime(i):
            res.append(i)
    return sorted(res)