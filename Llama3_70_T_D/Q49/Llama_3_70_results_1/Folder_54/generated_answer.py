def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(34)
    return decimal_number % fibonacci_number == 0