def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_139 = fibonacci(139)
    decimal_value = int(binary_rep, 2)
    return decimal_value % fib_139 == 0