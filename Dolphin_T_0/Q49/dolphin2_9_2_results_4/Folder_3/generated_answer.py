def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    index = 35
    a, b = (0, 1)
    while index > 1:
        a, b = (b, a + b)
        index -= 1
    return decimal % b == 0