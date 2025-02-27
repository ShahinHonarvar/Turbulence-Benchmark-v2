def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_84 = 1836311903
    return decimal_value % fibonacci_84 == 0