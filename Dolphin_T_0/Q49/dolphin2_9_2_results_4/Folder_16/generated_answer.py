def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a = 0
    b = 1
    i = 0
    while i < 128:
        a, b = (b, a + b)
        i += 1
    return decimal % b == 0