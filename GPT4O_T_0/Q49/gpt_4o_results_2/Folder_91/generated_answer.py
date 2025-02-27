def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_sixth = 8
    return decimal_number % fibonacci_sixth == 0