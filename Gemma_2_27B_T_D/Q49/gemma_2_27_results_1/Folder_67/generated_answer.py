def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_107 = 1074444626320579980
    return decimal_number % fibonacci_107 == 0