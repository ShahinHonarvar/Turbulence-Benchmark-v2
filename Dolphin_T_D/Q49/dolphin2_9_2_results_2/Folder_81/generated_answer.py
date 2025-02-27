def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    i = 0
    a, b = (0, 1)
    while i < n:
        a, b = (b, a + b)
        i += 1
    return n % b == 0