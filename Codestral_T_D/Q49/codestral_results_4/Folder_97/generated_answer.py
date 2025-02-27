def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_rep, 2)
    fibo_114 = fibonacci(114)
    return decimal % fibo_114 == 0