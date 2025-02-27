def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_15th_number = 610
    return decimal_number % fibonacci_15th_number == 0