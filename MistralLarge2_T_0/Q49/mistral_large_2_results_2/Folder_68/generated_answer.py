def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_38 = fibonacci(38)
    return decimal_value % fib_38 == 0