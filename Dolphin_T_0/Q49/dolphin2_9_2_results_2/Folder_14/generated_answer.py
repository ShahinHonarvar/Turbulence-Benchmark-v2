def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    a, b = (0, 1)
    i = 0
    while i < 27:
        a, b = (b, a + b)
        i += 1
    return n % a == 0