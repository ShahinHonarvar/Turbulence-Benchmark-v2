def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal = int(binary_string, 2)
    fibonacci_199 = fibonacci(199)
    return decimal % fibonacci_199 == 0