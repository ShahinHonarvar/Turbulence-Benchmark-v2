def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_125 = 14472334024676220991
    return decimal % fibonacci_125 == 0