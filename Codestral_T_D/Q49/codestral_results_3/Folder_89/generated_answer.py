def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_string, 2)
    fib_126 = fibonacci(126)
    return decimal % fib_126 == 0