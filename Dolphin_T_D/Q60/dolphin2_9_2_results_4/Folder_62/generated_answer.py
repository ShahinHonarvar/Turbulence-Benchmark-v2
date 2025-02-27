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
    x = tup[70]
    res = []
    for i in range(2, x + 1):
        if is_prime(i) and all((is_prime(int(str(i)[1:-1])) and len(str(i).replace('0', '')) != 0 for _ in range(len(str(i)) - 2))):
            res.append(i)
    return res