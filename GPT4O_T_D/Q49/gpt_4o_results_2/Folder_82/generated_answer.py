def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fibonacci_99 = fibonacci(99)
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_99 == 0