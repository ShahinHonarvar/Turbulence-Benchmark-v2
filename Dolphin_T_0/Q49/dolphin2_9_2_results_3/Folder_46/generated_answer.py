def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(139):
        a, b = (b, a + b)
    fibonacci_139 = a
    if decimal % fibonacci_139 == 0:
        return True
    else:
        return False