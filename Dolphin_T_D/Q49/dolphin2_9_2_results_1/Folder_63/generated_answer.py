def if_decimal_is_divisible(binary_rep):
    n = len(binary_rep)
    decimal = 0
    for i in range(n):
        decimal += int(binary_rep[n - 1 - i]) * pow(2, i)
    a, b = (0, 1)
    for _ in range(144):
        a, b = (b, a + b)
    return decimal % b == 0