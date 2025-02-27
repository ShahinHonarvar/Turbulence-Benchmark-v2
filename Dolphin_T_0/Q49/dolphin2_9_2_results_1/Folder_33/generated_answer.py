def fibonacci_sequence():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary):
    fib = fibonacci_sequence()
    for _ in range(133):
        next(fib)
    n = 0
    for digit in binary:
        n = n << 1 | int(digit)
    return n % next(fib) == 0