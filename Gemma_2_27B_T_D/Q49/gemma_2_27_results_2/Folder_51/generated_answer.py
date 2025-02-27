def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_17 = 1597
    return decimal_integer % fibonacci_17 == 0