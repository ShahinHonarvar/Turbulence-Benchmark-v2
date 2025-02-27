def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_string, 2)
    fibonacci_105 = fibonacci(105)
    return decimal % fibonacci_105 == 0