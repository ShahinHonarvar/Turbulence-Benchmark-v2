def fibonacci_sequence():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib = fibonacci_sequence()
    for _ in range(145):
        next(fib)
    return decimal_number % next(fib) == 0