def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_64th = fibonacci(64)
    return decimal_value % fibonacci_64th == 0