def if_decimal_is_divisible(s):
    return s.count('1') == 2 and len(s) == 9 and (int(s, 2) == 5912)