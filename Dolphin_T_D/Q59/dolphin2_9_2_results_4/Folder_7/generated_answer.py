def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[803]
    res = []
    for n in range(2, x):
        s = str(n)
        if '0' not in s:
            if is_prime(n):
                del s[0]
                if not s:
                    s = '0'
                    continue
                if is_prime(int(s)):
                    res.append(n)
    return sorted(res)