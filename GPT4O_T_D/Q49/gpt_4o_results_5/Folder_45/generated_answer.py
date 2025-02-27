def if_decimal_is_divisible(binary_str):
    fibonacci_28th = 317811
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_28th == 0