def if_decimal_is_divisible(binary_str):
    index = 186
    a, b = (0, 1)
    while index > 0:
        a, b = (b, a + b)
        index -= 1
    decimal = int(binary_str, 2)
    return decimal % b == 0