def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_118 = fibonacci(118)
    decimal_value = int(binary_representation, 2)
    return decimal_value % fib_118 == 0