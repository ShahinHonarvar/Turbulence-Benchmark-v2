def if_decimal_is_divisible(s):
    n = int(s, 2)
    i = 0
    a, b = (0, 1)
    while i < 37:
        i += 1
        a, b = (b, a + b)
    return n % b == 0