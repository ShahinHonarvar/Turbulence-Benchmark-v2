def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_68 = 20365011074
    return decimal % fibonacci_68 == 0