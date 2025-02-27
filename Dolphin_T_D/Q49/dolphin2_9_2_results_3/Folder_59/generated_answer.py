def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    num = 0
    a = 0
    b = 1
    while num < 73:
        a, b = (b, a + b)
        num += 1
    return decimal % b == 0