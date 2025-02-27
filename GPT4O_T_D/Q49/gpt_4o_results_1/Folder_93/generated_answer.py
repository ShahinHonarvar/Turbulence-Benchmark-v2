def if_decimal_is_divisible(binary_string):
    fibonacci_number = 956722026041
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_number == 0