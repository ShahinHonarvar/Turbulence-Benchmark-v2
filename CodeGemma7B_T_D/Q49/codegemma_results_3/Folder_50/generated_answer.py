def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        f, s = (0, 1)
        for _ in range(n):
            f, s = (s, f + s)
        return f
    n = int(binary_string, 2)
    fib = fibonacci(119)
    return n % fib == 0