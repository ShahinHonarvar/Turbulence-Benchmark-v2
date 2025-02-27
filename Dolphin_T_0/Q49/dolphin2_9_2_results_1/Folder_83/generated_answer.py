def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(60):
        a, b = (b, a + b)
    if decimal_integer % a == 0:
        return True
    else:
        return False