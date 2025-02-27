def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n_190_fib = fibonacci(190)
    decimal_value = int(binary_string, 2)
    return decimal_value % n_190_fib == 0