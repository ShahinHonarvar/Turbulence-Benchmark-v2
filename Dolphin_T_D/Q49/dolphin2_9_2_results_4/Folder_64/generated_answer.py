def if_decimal_is_divisible(n):
    a, b = (0, 1)
    i = 0
    while i < 10:
        a, b = (b, a + b)
        i += 1
    n = int(n, 2)
    return n % a == 0