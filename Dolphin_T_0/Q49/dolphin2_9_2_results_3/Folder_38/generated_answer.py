def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    i = 77
    a, b = (0, 1)
    for _ in range(77):
        a, b = (b, a + b)
    fibonacci = b
    return decimal % fibonacci == 0