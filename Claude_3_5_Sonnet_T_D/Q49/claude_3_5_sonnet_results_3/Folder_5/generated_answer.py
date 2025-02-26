def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_85 = fibonacci(85)
    return decimal % fib_85 == 0