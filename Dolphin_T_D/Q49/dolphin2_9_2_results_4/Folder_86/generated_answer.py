def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    a, b = (0, 1)
    for _ in range(135):
        a, b = (b, a + b)
    return decimal_num % b == 0