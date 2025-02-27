def if_decimal_is_divisible(binary_num):
    n = 104
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    decimal_num = int(binary_num, 2)
    return decimal_num % a == 0