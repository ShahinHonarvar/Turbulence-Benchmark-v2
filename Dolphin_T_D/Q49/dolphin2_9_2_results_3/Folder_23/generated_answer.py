def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    a, b = (0, 1)
    for _ in range(48):
        a, b = (b, a + b)
    return decimal_number % a == 0