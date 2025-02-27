def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_95 = 2364918987
    return decimal_number % fibonacci_95 == 0