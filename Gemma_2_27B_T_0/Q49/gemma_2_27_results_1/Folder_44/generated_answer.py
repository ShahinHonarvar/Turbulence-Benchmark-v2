def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_159 = 1548008755920
    return decimal_number % fibonacci_159 == 0