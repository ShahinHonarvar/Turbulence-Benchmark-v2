def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    a, b = (0, 1)
    for _ in range(93):
        a, b = (b, a + b)
    return n % a == 0