def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[25]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                if not is_prime(int(str(s)[1:-1])) or s[0] == '0' or s[-1] == '0':
                    break
                s = str(s)[1:-1]
            else:
                res.append(i)
    return sorted(res, reverse=True)