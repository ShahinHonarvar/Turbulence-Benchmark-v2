def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_189 = 129876077602553
    return decimal_number % fibonacci_189 == 0