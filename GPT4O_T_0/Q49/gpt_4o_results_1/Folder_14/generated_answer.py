def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_27th = 317811
    return decimal_number % fibonacci_27th == 0