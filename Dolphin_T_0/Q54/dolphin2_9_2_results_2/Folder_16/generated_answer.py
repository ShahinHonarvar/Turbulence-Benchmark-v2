def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[792]
    res = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    break
            else:
                res.append(i)
    return sorted(res)