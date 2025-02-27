def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_14 = (5 * ((1 + 5 ** 0.5) / 2) ** 3 + 3) / 2 - (5 * (1 + 5 ** 0.5) / 2 + 6) / 2 + 7
    return decimal % fibonacci_14 == 0 if fibonacci_14 != 0 else False