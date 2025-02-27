def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a = 0
    b = 1
    for _ in range(64):
        a, b = (b, a + b)
    fibonacci_64th = a
    return decimal % fibonacci_64th == 0