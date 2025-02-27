def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_19th = 4181
    return decimal % fibonacci_19th == 0