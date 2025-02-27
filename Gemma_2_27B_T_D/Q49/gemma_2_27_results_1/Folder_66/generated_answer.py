def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_120 = 108576025845172404
    return decimal_value % fibonacci_120 == 0