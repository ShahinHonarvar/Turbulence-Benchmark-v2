def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    i = 195
    a, b = (0, 1)
    while i > 1:
        a, b = (b, a + b)
        i -= 1
    return decimal_integer % b == 0