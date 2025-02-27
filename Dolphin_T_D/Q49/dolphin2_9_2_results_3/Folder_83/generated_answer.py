def if_decimal_is_divisible(binary_string):
    i = 0
    a, b = (0, 1)
    while i < 59:
        a, b = (b, a + b)
        i += 1
    decimal = int(binary_string, 2)
    return decimal % b == 0