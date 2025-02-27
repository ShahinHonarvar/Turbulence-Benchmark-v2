def if_decimal_is_divisible(binary):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n = int(binary, 2)
    fib_137 = fibonacci(137)
    return n % fib_137 == 0