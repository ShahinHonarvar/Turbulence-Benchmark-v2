def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_54 = 1094617711930473686
    return decimal_number % fibonacci_54 == 0