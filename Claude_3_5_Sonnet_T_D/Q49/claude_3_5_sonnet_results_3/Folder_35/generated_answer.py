def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_string, 2)
    fibonacci_187 = fibonacci(187)
    return decimal_value % fibonacci_187 == 0