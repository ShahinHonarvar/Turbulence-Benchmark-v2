def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_95 = fibonacci(95)
    return decimal % fib_95 == 0