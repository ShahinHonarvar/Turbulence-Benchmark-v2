def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_representation, 2)
    fibonacci_175 = fibonacci(175)
    return decimal_number % fibonacci_175 == 0