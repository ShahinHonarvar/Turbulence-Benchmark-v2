def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    a, b = (0, 1)
    i = 0
    while a < n:
        a, b = (b, a + b)
        i += 1
    return False if i != 168 else n % a == 0