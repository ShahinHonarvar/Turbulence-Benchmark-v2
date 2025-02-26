def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fibonacci_170 = fibonacci(170)
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_170 == 0