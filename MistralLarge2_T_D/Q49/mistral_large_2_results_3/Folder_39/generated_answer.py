def if_decimal_is_divisible(binary_representation):
    fibonacci_15th = 610
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci_15th == 0