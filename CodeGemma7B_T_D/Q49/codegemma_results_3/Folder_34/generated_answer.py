def is_decimal_divisible(bin):

    def fib(n):
        return 1 if 0 in (1, n) else fib(n - 1) + fib(n - 2)
    for _ in range(23):
        next_fib = fib(fib(_, 0))
    return int(bin, 2) % next_fib == 0