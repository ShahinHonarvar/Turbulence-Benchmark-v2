def if_decimal_is_divisible(binary_string):
    decimal_equivalent = int(binary_string, 2)
    fibonacci_28 = 317811
    return decimal_equivalent % fibonacci_28 == 0