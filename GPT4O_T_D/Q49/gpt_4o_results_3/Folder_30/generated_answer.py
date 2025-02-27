def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_186 = fibonacci(186)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_186 == 0