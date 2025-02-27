def if_decimal_is_divisible(binary_string):
    a, b = (0, 1)
    for _ in range(177):
        a, b = (b, a + b)
    decimal = int(binary_string, 2)
    return decimal % b == 0