def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_189 = 1836311903
    return decimal_integer % fibonacci_189 == 0