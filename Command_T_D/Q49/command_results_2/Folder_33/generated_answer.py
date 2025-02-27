def if_decimal_is_divisible(s):
    return bool(s) and s[0] == '1' and (int(s[1:], 2) == 34)