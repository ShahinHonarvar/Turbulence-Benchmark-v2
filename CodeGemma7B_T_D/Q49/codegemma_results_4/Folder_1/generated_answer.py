import math

def if_decimal_is_divisible(binary_representation):
    """
    >>> if_decimal_is_divisible("101")
    False

    >>> if_decimal_is_divisible("1101")
    True
    """
    a = 0
    b = 1
    cnt = 0
    while cnt < 90:
        a, b = (b, a + b)
        if a % 90 == 0:
            return True
        cnt += 1
    return False