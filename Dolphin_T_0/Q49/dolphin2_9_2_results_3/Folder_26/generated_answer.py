def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary):
    n, fib = (int(binary, 2), fibonacci())
    while n != next(fib):
        pass
    return n % 138 == 0