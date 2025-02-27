def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple, x):
    trunc_p = []
    for num in range(1, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while str_num and is_prime(num):
            trunc_p.append(num)
            str_num = str_num[1:-1]
            num = int(str_num)
    trunc_p.sort()
    return trunc_p