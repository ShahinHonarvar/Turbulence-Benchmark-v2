def all_left_truncatable_prime(tup):
    x = tup[36]

    def is_prime(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    res = []
    for i in range(2, x):
        if not i.__str__().__contains__('0'):
            tmp = i
            is_truncatable = True
            for j in range(len(str(i))):
                tmp //= 10
                if not is_prime(tmp):
                    is_truncatable = False
                    break
            if is_truncatable:
                res.append(i)
    return sorted(res, reverse=True)