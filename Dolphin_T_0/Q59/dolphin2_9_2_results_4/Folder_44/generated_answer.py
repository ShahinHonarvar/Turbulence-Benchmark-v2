def all_left_truncatable_prime(t):

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[39]
    res = []
    for i in range(2, x):
        if check_prime(i):
            s = str(i)
            flag = True
            for j in range(1, len(s)):
                if not check_prime(int(s[j:])):
                    flag = False
                    break
            if flag:
                res.append(i)
    return res