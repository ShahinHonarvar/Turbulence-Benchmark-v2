def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[55]
    res = []
    for i in range(2, x):
        if is_prime(i) and i % 10:
            s = str(i)
            while s:
                if not is_prime(int(s)):
                    break
                s = s[1:]
            else:
                res.append(i)
    return sorted(res)