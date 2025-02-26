def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_87 = fibonacci(87)
    return decimal % fib_87 == 0