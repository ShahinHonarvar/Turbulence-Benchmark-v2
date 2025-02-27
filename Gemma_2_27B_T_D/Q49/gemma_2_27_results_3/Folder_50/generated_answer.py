def if_decimal_is_divisible(binary_string):
    decimal_equivalent = int(binary_string, 2)
    fibonacci_119 = 46368
    return decimal_equivalent % fibonacci_119 == 0