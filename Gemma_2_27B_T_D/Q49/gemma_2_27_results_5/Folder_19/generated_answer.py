def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_29 = 514229
    return decimal % fibonacci_29 == 0