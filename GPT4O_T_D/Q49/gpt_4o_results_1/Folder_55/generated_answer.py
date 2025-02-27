def if_decimal_is_divisible(binary_str):
    fibonacci_39th = 39088169
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_39th == 0