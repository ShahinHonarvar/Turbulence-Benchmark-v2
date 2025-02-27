def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a = 0
    b = 1
    for _ in range(38):
        a, b = (b, a + b)
    return decimal % b == 0