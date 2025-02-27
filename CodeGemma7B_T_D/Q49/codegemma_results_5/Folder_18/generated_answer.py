def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    binary_int = int(binary_string, 2)
    fibonacci_199 = fibonacci(199)
    return binary_int % fibonacci_199 == 0