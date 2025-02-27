def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_76 = 165580141
    return decimal_number % fibonacci_76 == 0