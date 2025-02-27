def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_representation, 2)
    fib_196 = fibonacci(196)
    return decimal_number % fib_196 == 0