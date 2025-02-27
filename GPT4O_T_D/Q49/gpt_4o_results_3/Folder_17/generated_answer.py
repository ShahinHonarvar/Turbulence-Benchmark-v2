def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_154 = fibonacci(154)
    return decimal_num % fibonacci_154 == 0