def if_decimal_is_divisible(binary_string):
    decimal_equivalent = int(binary_string, 2)
    fibonacci_40 = 102334155
    return decimal_equivalent % fibonacci_40 == 0