def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_196 = 1062700897
    return decimal_number % fibonacci_196 == 0