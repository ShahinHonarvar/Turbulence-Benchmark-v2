def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_147 = 1394232245130359299
    return decimal_number % fibonacci_147 == 0