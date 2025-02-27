def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_28 = 317811
    return decimal % fibonacci_28 == 0