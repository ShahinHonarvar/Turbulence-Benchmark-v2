def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(49):
        a, b = (b, a + b)
    return decimal_integer % b == 0