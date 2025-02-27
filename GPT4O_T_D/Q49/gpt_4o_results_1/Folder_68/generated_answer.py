def if_decimal_is_divisible(binary_str):
    fibonacci_38th = 39088169
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_38th == 0