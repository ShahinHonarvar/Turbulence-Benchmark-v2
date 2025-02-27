def if_decimal_is_divisible(binary):

    def get_next_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib = get_next_fibonacci()
    decimal = int(binary, 2)
    for i in range(76):
        next(fib)
    return decimal % next(fib) == 0