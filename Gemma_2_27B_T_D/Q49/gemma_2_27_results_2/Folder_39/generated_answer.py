def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_15 = 610
    return decimal_num % fibonacci_15 == 0