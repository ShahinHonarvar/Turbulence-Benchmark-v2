def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    i = 3
    a, b = (0, 1)
    while i > 0:
        a, b = (b, a + b)
        i -= 1
    return decimal % a == 0