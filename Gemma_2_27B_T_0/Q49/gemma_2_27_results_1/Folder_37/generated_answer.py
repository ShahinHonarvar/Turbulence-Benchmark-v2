def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_46 = 1836311903
    return decimal_number % fibonacci_46 == 0