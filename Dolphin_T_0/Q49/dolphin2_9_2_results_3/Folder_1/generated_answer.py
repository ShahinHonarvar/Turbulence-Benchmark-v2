def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a, b = (0, 1)
    for _ in range(89):
        a, b = (b, a + b)
    fibonacci_89 = b
    return decimal % fibonacci_89 == 0