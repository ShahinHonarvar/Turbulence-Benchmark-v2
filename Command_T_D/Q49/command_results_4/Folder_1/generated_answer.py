def if_decimal_is_divisible(s):
    return s[::-1] == str(int(s[::-1], 2)) % '10'