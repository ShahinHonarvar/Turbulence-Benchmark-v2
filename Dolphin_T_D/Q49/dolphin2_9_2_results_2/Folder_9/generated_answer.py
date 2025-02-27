def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    i = 0
    a, b = (0, 1)
    while i < 68:
        a, b = (b, a + b)
        i += 1
    return decimal % a == 0