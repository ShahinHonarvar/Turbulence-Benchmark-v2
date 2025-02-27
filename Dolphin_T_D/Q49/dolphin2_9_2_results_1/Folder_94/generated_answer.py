def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    a, b = (0, 1)
    i = 0
    while i < 40:
        a, b = (b, a + b)
        i += 1
    return decimal_number % a == 0