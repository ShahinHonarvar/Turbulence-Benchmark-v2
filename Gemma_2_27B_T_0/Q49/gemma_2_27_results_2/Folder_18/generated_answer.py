def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_199 = 9671406561
    return decimal_number % fibonacci_199 == 0