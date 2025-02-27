def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_108 = 165580141
    return decimal_number % fibonacci_108 == 0