def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_27 = 196418
    return decimal_number % fibonacci_27 == 0