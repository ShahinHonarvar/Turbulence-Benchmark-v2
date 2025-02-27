def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_104 = fibonacci(104)
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fib_104 == 0