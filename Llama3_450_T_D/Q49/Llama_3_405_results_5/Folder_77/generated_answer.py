def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_110 = fibonacci(110)
    decimal = int(binary_string, 2)
    return decimal % fib_110 == 0