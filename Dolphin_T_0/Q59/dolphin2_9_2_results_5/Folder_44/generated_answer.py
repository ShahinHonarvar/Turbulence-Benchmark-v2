def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[39]
    res = []
    for num in range(2, x):
        if is_prime(num):
            num_s = str(num)
            if '0' not in num_s:
                trunc = num_s[1:]
                while trunc and is_prime(int(trunc)):
                    trunc = trunc[1:]
                    if len(trunc) == 0:
                        res.append(num)
    return sorted(res)