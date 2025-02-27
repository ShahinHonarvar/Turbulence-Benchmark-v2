def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_175 = fibonacci(175)
    return decimal_number % fibonacci_175 == 0