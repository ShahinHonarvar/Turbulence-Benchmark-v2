def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fibonacci_118 = fibonacci(118)
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_118 == 0