def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_154 = 2519226460460349647472094094772371005847
    return decimal_integer % fibonacci_154 == 0