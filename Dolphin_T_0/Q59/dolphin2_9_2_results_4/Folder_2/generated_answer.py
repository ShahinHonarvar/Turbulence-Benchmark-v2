def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[618]
    res = []
    for i in range(2, x):
        if is_prime(i):
            y = i
            while y:
                if y % 10 == 0:
                    y //= 10
                else:
                    return
                if not is_prime(y):
                    break
                y //= 10
            else:
                res.append(i)
    return sorted(res)