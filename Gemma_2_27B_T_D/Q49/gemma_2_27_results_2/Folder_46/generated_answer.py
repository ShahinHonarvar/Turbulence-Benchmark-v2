def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_139 = 3570045132
    return decimal % fibonacci_139 == 0