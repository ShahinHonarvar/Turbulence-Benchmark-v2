def if_decimal_is_divisible(binary_str):
    decimal_integer = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_74th = fibonacci(74)
    return decimal_integer % fibonacci_74th == 0