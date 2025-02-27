def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n < 2 or n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    res = []
    for i in range(x, 0, -1):
        s = str(i)
        if '0' in s:
            continue
        s = s[1:-1]
        while len(s) > 1 and s[0] != s[-1]:
            if not is_prime(int(s)):
                break
            s = s[1:-1]
        if len(s) == 1 and is_prime(int(s)):
            res.append(i)
    return res