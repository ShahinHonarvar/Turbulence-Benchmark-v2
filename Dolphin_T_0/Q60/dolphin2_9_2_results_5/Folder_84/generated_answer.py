def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[630]
    ret = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 2:
            if not is_prime(int(str_num)):
                break
            str_num = str_num[1:-1]
        if is_prime(int(str_num)):
            ret.append(num)
    return ret[::-1]