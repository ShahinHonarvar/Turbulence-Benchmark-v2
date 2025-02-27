def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_integer = int(binary_str, 2)
    fibonacci_139 = fibonacci(139)
    return decimal_integer % fibonacci_139 == 0