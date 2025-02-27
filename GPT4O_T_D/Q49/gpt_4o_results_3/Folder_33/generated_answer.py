def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_134 = fibonacci(134)
    return decimal_number % fibonacci_134 == 0