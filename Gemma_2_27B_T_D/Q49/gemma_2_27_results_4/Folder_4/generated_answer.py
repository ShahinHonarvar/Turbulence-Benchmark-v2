def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_118 = 144759346
    return decimal_number % fibonacci_118 == 0