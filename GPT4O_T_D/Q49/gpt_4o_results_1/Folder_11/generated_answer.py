def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_16th = 610
    return decimal_number % fibonacci_16th == 0