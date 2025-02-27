def if_decimal_is_divisible(binary_string):
    n = len(binary_string)
    decimal = 0
    for i in range(0, n):
        decimal += int(binary_string[-i - 1]) * pow(2, i)
    a, b = (0, 1)
    for _ in range(114):
        a, b = (b, a + b)
    return decimal % b == 0