def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_107 = 107407408624768
    return decimal_number % fibonacci_107 == 0