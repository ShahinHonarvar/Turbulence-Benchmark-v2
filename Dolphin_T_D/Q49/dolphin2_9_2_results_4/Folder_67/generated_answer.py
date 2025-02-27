def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary):
    fib = fibonacci()
    for _ in range(106):
        next(fib)
    divisor = next(fib)
    return int(binary, 2) % divisor == 0