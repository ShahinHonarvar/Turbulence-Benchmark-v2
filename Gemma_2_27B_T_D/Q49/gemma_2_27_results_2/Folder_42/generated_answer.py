def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_146 = 1134903170
    return decimal % fibonacci_146 == 0