def if_decimal_is_divisible(binary):

    def fibonacci_gen():
        a, b = (0, 1)
        while True:
            yield b
            a, b = (b, a + b)
    fib = fibonacci_gen()
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    n = 0
    while True:
        term = next(fib)
        if term > decimal:
            break
        if term == decimal:
            n += 1
    return n % 138 == 0