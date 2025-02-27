def if_decimal_is_divisible(n):
    a, b = (0, 1)
    for _ in range(46):
        a, b = (b, a + b)
    fibonacci_46 = b
    return int(n, 2) % fibonacci_46 == 0