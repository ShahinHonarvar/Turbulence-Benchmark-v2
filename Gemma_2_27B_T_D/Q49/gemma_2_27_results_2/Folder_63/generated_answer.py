def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_144 = 1134903170
    return decimal_number % fibonacci_144 == 0