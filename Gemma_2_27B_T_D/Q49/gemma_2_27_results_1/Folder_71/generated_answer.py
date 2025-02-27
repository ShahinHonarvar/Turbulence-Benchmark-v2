def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    a = 0
    b = 1
    for i in range(147):
        a, b = (b, a + b)
    return decimal_integer % b == 0