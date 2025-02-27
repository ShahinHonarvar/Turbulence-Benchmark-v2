def if_decimal_is_divisible(binary_num):
    num = int(binary_num, 2)
    a, b = (0, 1)
    for _ in range(86):
        a, b = (b, a + b)
    return num % b == 0