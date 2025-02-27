def if_decimal_is_divisible(binary_string):
    num_fibonacci = 149
    a, b = (0, 1)
    while num_fibonacci > 0:
        a, b = (b, a + b)
        num_fibonacci -= 1
    decimal_integer = int(binary_string, 2)
    return decimal_integer % b == 0