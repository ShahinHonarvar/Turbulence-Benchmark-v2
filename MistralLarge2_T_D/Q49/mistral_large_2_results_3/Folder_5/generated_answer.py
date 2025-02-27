def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_integer = int(binary_rep, 2)
    fibonacci_85 = fibonacci(85)
    return decimal_integer % fibonacci_85 == 0