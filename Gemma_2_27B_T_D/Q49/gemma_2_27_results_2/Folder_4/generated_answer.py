def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_118 = 1974027421987
    return decimal % fibonacci_118 == 0