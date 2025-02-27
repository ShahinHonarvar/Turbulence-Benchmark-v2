def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_117th = fibonacci(117)
    return decimal % fib_117th == 0