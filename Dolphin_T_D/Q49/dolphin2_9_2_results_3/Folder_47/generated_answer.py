def if_decimal_is_divisible(binary):
    n = 94
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    fib = b
    decimal = int(binary, 2)
    return decimal % fib == 0