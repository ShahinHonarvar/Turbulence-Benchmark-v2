def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_109 = fibonacci(109)
    return decimal % fib_109 == 0