def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_108 = 342051965471
    return decimal_value % fibonacci_108 == 0