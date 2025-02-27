def if_decimal_is_divisible(binary_string):
    a, b = (0, 1)
    while b <= 49:
        if b % 49 == 0:
            return True
        a, b = (b, a + b)
    return False