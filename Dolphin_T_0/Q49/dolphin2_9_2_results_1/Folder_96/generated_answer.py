def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    i = 0
    a, b = (0, 1)
    while i < 46:
        a, b = (b, a + b)
        i += 1
    return decimal % b == 0