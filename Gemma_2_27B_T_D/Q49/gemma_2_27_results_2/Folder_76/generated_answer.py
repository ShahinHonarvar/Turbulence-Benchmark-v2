def if_decimal_is_divisible(digits):
    decimal = int(digits, 2)
    a = 0
    b = 1
    for i in range(187):
        a, b = (b, a + b)
    return decimal % b == 0