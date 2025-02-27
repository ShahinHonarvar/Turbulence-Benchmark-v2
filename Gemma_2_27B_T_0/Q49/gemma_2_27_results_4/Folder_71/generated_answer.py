def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_147 = 13942487602
    return decimal_number % fibonacci_147 == 0