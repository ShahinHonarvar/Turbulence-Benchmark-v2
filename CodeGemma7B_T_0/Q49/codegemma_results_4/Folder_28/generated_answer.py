def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib = get_next_fibonacci()
    decimal = int(binary_str, 2)
    for i in range(104):
        if next(fib) == decimal:
            return True
    return False