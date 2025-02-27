def if_decimal_is_divisible(binary_str):
    fibonacci_14th = 377
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_14th == 0