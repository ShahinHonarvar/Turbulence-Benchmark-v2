def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(80):
        a, b = (b, a + b)
    return n % b == 0