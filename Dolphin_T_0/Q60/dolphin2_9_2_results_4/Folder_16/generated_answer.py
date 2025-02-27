def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[792]
    res = []
    for i in range(2, x):
        if is_prime(i) and ''.join(filter(lambda x: x != '0', str(i))).isdigit() and (is_prime(int(str(i)[1:-1])) or int(str(i)[1:-1]) < 2):
            res.append(i)
    return sorted(res)