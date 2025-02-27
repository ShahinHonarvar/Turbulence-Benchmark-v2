def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, round(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        return True
    x = t[77]
    res = []
    for i in range(x, 0, -1):
        s = str(i)
        if '0' in s:
            continue
        while True:
            if len(s) <= 2:
                if is_prime(int(s)):
                    res.append(int(s))
                break
            if not is_prime(int(s)):
                break
            if not is_prime(int(s[1:])):
                break
            if not is_prime(int(s[:-1])):
                break
            s = s[1:-1]
    return res