def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    a, b = (0, 1)
    for _ in range(64):
        a, b = (b, a + b)
    fibonacci_64 = a
    return decimal % fibonacci_64 == 0