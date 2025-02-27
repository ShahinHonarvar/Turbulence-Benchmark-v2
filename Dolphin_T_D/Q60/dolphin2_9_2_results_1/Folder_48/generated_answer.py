def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[835]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            while len(str_i) > 1:
                if '0' in str_i:
                    break
                if not is_prime(int(str_i[1:])):
                    break
                if not is_prime(int(str_i[:-1])):
                    break
                str_i = str_i[1:-1]
            else:
                res.append(i)
    return sorted(res)