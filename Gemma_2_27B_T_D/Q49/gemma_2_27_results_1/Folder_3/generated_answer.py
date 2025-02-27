def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_35 = 9227465
    return decimal % fibonacci_35 == 0