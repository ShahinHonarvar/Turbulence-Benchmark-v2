def if_decimal_is_divisible(binary_str):
    a = 0
    b = 1
    for _ in range(176):
        a, b = (b, a + b)
    decimal = int(binary_str, 2)
    return decimal % b == 0