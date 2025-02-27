def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_54 = 17711
    return decimal_number % fibonacci_54 == 0