def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    i = 0
    a, b = (0, 1)
    while i < 89:
        a, b = (b, a + b)
        i += 1
    return decimal_number % b == 0