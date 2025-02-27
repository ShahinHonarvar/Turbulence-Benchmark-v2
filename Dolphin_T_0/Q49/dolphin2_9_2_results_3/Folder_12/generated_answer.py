def if_decimal_is_divisible(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    fib66 = 0
    a, b = (0, 1)
    for i in range(66):
        a, b = (b, a + b)
        fib66 = b
    return decimal % fib66 == 0