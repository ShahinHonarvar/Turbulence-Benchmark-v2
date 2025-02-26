def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fibonacci_17th = fibonacci(17)
    return decimal_number % fibonacci_17th == 0