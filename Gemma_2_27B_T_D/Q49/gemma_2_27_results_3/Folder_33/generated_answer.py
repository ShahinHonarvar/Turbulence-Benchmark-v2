def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_134 = 173901021791616034422722
    return decimal % fibonacci_134 == 0