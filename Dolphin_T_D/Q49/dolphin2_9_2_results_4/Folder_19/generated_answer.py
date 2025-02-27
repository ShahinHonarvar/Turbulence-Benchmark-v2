def if_decimal_is_divisible(n):
    a = 0
    b = 1
    for i in range(29):
        a, b = (b, a + b)
    decimal = int(n, 2)
    return decimal % b == 0