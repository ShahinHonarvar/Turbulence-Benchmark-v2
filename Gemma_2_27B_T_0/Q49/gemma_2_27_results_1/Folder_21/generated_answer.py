def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_195 = 1062508072963781250
    return decimal_number % fibonacci_195 == 0