def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(134):
        a, b = (b, a + b)
    return decimal % b == 0