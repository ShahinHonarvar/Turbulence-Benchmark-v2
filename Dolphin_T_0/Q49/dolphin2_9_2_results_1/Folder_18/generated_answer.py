def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(199):
        a, b = (b, a + b)
    return decimal_int % b == 0