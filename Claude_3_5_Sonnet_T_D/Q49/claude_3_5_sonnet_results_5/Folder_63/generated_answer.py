def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_string, 2)
    fibonacci_144 = fibonacci(144)
    return decimal_value % fibonacci_144 == 0