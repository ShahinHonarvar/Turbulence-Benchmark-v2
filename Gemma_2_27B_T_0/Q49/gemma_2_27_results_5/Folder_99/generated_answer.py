def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_109 = 10946
    return decimal_number % fibonacci_109 == 0