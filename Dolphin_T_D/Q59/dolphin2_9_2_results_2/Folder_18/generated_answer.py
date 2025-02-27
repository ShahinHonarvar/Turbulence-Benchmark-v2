def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[429]
    res = []
    for num in range(x, 0, -1):
        if is_prime(num):
            str_num = str(num)
            if '0' in str_num or len(str_num) == 1:
                continue
            flag = True
            for i in range(len(str_num) - 1):
                if not is_prime(int(str_num[i:])):
                    flag = False
                    break
            if flag:
                res.append(num)
    return res