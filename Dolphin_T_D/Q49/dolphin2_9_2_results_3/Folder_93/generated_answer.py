def if_decimal_is_divisible(binary):
    decimal_num = int(binary, 2)
    a, b = (0, 1)
    for _ in range(59):
        a, b = (b, a + b)
    return decimal_num % b == 0