def all_left_truncatable_prime(t):

    def is_prime(a):
        if a <= 1:
            return False
        elif a <= 3:
            return True
        elif a % 2 == 0 or a % 3 == 0:
            return False
        i = 5
        while i * i <= a:
            if a % i == 0 or a % (i + 2) == 0:
                return False
            i += 6
        return True

    def trunc(s):
        if not s:
            return None
        while not is_prime(int(s)):
            s = s[1:]
        return s
    res = []
    x = t[69]
    for i in range(x, 0, -1):
        if trunc(str(i)) is not None:
            res.append(i)
    return res[::-1]