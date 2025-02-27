def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_rep, 2)
    fib_188 = fibonacci(188)
    return decimal % fib_188 == 0