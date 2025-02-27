def if_decimal_is_divisible(binary_str):
    decimal_val = int(binary_str, 2)
    a = 0
    b = 1
    for i in range(179):
        a, b = (b, a + b)
    return decimal_val % b == 0