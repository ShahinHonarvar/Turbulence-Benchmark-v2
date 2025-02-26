def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal = int(binary_string, 2)
    fib_150 = fibonacci(150)
    return decimal % fib_150 == 0