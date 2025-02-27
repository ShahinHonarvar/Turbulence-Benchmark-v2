def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    i = 0
    a, b = (0, 1)
    while i < 154:
        a, b = (b, a + b)
        i += 1
    return n % a == 0