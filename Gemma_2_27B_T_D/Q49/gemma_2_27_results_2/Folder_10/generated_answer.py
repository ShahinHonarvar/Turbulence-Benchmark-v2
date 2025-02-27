def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_88 = 18473521491093768
    return decimal_value % fibonacci_88 == 0