def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_string, 2)
    fib_48 = fibonacci(48)
    return decimal % fib_48 == 0