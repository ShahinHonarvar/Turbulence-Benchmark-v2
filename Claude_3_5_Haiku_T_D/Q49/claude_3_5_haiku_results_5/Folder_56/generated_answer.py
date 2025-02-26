def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    fib_84 = fibonacci(84)
    return decimal_value % fib_84 == 0