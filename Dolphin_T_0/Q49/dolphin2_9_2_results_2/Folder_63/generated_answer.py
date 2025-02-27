def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    i = 0
    a = 0
    b = 1
    while i < 143:
        c = a + b
        a = b
        b = c
        i += 1
    return n % b == 0