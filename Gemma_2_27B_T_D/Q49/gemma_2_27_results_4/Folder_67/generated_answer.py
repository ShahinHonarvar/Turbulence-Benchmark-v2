def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_107 = 142727106409690811473982220563183
    return decimal % fibonacci_107 == 0