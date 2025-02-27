def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_13th = 233
    return decimal % fibonacci_13th == 0