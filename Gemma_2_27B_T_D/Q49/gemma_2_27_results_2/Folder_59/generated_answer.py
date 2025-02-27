def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_74 = 1836311903
    return decimal % fibonacci_74 == 0