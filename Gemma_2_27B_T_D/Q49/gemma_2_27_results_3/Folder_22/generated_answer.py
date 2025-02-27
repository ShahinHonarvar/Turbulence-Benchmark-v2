def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_20 = 6765
    return decimal % fibonacci_20 == 0