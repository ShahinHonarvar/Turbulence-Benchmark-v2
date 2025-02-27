def if_decimal_is_divisible(binary):
    fib, p1, p2 = (0, 0, 1)
    num = int(binary, 2)
    while num >= fib:
        fib += p1 + p2
        p1 = p2
        p2 = fib - p1
    return num == fib