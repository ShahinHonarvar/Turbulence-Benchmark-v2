def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[37]
    res = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            str_num = str(num)
            while len(str_num) > 1:
                if str_num[0] == '0':
                    break
                str_num = str_num[1:]
                if not is_prime(int(str_num)):
                    break
            else:
                res.append(num)
    return res