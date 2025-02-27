def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_97 = 1069069017
    return decimal_number % fibonacci_97 == 0