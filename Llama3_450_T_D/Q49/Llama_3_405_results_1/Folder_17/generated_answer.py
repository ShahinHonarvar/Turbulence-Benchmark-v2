def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_154 = fibonacci(154)
    decimal = int(binary_string, 2)
    return decimal % fib_154 == 0