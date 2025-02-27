def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncat(n):
        return int(str(n)[1:])
    x = t[22]
    res = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and (not str(i).count('0')):
            while i > 1:
                if not is_prime(left_truncat(i)):
                    break
                i = left_truncat(i)
            else:
                res.append(i)
    return res