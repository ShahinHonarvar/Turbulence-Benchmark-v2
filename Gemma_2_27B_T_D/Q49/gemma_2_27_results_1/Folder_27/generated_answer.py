def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_87 = 10000000093139
    return decimal_value % fibonacci_87 == 0