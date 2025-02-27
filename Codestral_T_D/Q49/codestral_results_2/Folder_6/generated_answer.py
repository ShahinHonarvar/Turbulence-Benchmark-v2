def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    decimal_integer = int(binary_representation, 2)
    fib_185 = fibonacci(185)
    return decimal_integer % fib_185 == 0