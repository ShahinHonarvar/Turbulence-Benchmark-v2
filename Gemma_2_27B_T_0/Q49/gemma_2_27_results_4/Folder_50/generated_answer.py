def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_119 = 1061020984
    return decimal_number % fibonacci_119 == 0