def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_46 = 1836311903
    return decimal % fibonacci_46 == 0