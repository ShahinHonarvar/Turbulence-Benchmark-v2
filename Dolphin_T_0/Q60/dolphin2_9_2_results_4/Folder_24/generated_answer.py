def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    x = tup[65]
    res = [i for i in range(2, x + 1) if is_prime(i) and i > 9 and (i < 100) and ('0' not in str(i) and len(str(i)) == 2 and (is_prime(int(str(i)[1])) and is_prime(int(str(i)[0]))))]
    for i in res:
        n = int(str(i)[0] + str(i)[1])
        while n > 1:
            if is_prime(n) and n not in res:
                res.append(n)
            n = int(str(n)[1] + str(n)[2])
    return sorted(res, reverse=True)