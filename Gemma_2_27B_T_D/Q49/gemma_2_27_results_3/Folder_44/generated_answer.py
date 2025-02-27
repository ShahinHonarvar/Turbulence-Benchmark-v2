def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_159 = 250473082917606001298488079709
    return decimal_integer % fibonacci_159 == 0