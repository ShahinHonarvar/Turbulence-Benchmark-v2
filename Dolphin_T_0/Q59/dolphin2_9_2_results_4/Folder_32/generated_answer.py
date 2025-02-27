def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[42]
    res = []
    for i in range(2, x):
        if all([is_prime(int(str(i)[j:])) for j in range(len(str(i)))]) and i not in res:
            res.append(i)
    return res