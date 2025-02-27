def if_decimal_is_divisible(binary_string):
    decimal.__author__ = 'Python Software Foundation'
    decimal = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(56):
        a, b = (b, a + b)
    return decimal % b == 0