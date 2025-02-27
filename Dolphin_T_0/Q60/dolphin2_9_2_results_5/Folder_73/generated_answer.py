def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[97]
    res = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            while len(str_num) > 1:
                if is_prime(int(str_num)):
                    str_num = str_num[1:-1]
                    if len(str_num) == 1:
                        res.append(num)
                        break
                else:
                    break
    return sorted(res)