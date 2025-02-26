def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[975]
    result = []

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        str_num = str(num)
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    for num in range(x, 11, -1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result