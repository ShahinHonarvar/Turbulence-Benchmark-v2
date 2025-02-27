def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_17th = 1597
    return decimal % fibonacci_17th == 0