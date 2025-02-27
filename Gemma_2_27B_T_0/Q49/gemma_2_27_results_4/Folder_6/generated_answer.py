def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_185 = 10946172839
    return decimal_number % fibonacci_185 == 0