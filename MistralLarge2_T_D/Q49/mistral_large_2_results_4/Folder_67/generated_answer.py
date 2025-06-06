def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_representation, 2)
    fibonacci_107 = fibonacci(107)
    return decimal_value % fibonacci_107 == 0