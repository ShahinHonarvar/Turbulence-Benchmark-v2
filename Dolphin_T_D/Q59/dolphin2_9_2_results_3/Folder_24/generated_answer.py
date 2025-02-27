def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = int(t[65])
    res = []
    for i in range(x, 1, -1):
        if i == 0:
            continue
        s = str(i)
        if not is_prime(i):
            continue
        for j in range(len(s) - 1):
            if not is_prime(int(s[j:])):
                break
        else:
            res.append(i)
    return res