def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = 0
    a, b = (0, 1)
    i = 0
    while i < 47:
        fibonacci = a
        a, b = (b, a + b)
        i += 1
    return decimal % fibonacci == 0