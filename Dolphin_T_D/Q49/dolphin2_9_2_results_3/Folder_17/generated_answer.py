def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(153):
        a, b = (b, a + b)
    if decimal % b == 0:
        return True
    else:
        return False