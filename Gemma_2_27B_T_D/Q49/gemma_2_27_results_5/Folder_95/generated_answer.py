def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_168 = 2178309234248
    return decimal % fibonacci_168 == 0