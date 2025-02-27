def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a, b = (0, 1)
    for _ in range(20):
        a, b = (b, a + b)
    fibonacci_number = b
    if decimal % fibonacci_number == 0:
        return True
    else:
        return False