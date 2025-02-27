def if_decimal_is_divisible(x):
    fib, a, b = (0, 0, 1)
    for _ in range(154):
        fib = a + b
        a, b = (b, fib)
    d = x
    value = 0
    while d > 0:
        temp = d % 10
        value = value * 2 + temp
        d //= 10
    if value % fib == 0:
        return True
    else:
        return False