def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_representation, 2)
    fibonacci_number = fibonacci(168)
    return decimal_number % fibonacci_number == 0