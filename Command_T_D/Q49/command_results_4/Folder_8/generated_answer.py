def if_decimal_is_divisible(s):
    return bin(int(s, 2)).count('1') % 54 == 0