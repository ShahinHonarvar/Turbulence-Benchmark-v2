def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_56 = 10488849195791
    return decimal_number % fibonacci_56 == 0