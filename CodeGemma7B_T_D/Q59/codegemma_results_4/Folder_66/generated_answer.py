def left_truncatable(num):
    str_num = str(num)
    for i, digit in enumerate(str_num):
        if int(digit) == 0 or not is_prime(int(str_num[i:])):
            return False
    return True