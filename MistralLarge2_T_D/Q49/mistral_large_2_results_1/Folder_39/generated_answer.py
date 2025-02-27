def if_decimal_is_divisible(binary_str):
    fibonacci_15th = 610
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_15th == 0