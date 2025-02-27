def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_rep, 2)
    fibonacci_150 = fibonacci(150)
    return decimal_value % fibonacci_150 == 0