import math

def is_prime_n(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[39]
    left_right_truncatable_prime_list = []
    if x < 2:
        return left_right_truncatable_prime_list
    for num in range(x, 1, -1):
        str_num = str(num)
        left_num = str_num[1:-1]
        right_num = str_num[0:-2]
        if '0' in str_num:
            continue
        if is_prime_n(num):
            left_num = left_num[0:-1] if str_num[0] == str_num[-1] else left_num
            if is_prime_n(int(left_num)) and is_prime_n(int(right_num)):
                left_right_truncatable_prime_list.append(num)
    return left_right_truncatable_prime_list