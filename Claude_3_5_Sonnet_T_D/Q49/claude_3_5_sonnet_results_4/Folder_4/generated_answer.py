def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_118 = fibonacci(118)
    decimal = int(binary_string, 2)
    return decimal % fib_118 == 0