def if_decimal_is_divisible(binary_rep):
    exponent = len(binary_rep) - 1
    decimal = 0
    for digit in binary_rep:
        decimal += int(digit) * 2 ** exponent
        exponent -= 1
    i = 0
    a, b = (0, 1)
    while i < 100:
        a, b = (b, a + b)
        i += 1
    return decimal % b == 0