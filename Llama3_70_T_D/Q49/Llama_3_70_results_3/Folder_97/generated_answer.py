def if_decimal_is_divisible(binary_string):
    a = 0
    b = 1
    for _ in range(114):
        a, b = (b, a + b)
    decimal = int(binary_string, 2)
    return decimal % b == 0