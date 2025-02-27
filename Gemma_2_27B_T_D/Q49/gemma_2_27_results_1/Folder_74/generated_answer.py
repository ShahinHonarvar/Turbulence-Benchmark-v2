def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    fibonacci_166 = 10946
    return decimal_representation % fibonacci_166 == 0