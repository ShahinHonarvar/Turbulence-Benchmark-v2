def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    fibonacci_17 = 1597
    return decimal_representation % fibonacci_17 == 0