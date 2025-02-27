def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_170 = 3645181390082757236979278101526479632
    return decimal_number % fibonacci_170 == 0