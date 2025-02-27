def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    fibonacci_84 = 20365011074
    return decimal_value % fibonacci_84 == 0