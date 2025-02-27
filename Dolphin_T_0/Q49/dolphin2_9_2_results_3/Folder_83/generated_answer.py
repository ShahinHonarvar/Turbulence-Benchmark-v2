def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    i = 0
    a, b = (0, 1)
    while i < 60:
        a, b = (b, a + b)
        i += 1
    fibonacci_60th = a
    return decimal % fibonacci_60th == 0