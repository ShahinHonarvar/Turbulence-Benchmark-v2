def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_107 = 137344400160
    return decimal % fibonacci_107 == 0