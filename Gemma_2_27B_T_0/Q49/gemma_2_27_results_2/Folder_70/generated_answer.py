def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_137 = 106094918977
    return decimal_number % fibonacci_137 == 0