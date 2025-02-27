def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    if decimal % 34 == 0:
        return True
    else:
        return False