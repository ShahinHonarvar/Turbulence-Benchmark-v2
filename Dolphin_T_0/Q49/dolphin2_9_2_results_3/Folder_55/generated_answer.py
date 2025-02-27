def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, base=2)
    a, b = (0, 1)
    for _ in range(39):
        a, b = (b, a + b)
    return decimal % a == 0