def if_decimal_is_divisible(s):
    return 1 << s[::-1].index('1') == 5922