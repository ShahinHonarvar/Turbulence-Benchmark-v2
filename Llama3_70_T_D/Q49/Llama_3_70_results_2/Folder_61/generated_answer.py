def if_decimal_is_divisible(binary_string):

    def fibonacci_sequence():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_sequence = fibonacci_sequence()
    for _ in range(76):
        next(fib_sequence)
    fib_76 = next(fib_sequence)
    decimal = int(binary_string, 2)
    return decimal % fib_76 == 0