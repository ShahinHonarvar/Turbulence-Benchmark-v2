def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_representation, 2)
    fibonacci_160th = fibonacci(160)
    return decimal_value % fibonacci_160th == 0