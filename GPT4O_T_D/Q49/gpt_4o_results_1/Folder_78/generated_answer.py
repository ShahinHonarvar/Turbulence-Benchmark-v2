def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_115 = fibonacci(115)
    return n % fibonacci_115 == 0