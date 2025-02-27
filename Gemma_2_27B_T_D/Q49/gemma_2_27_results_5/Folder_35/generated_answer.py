def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_187 = 1557 * 10 ** 11 + 555146
    return decimal_number % fibonacci_187 == 0