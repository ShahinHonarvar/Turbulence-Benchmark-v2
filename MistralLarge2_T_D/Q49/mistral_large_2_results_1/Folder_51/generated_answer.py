def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    fibonacci_17th = fibonacci(17)
    return decimal_number % fibonacci_17th == 0