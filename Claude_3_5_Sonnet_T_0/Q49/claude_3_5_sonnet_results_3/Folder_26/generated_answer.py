def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    fibonacci_138 = fibonacci(138)
    return decimal_number % fibonacci_138 == 0