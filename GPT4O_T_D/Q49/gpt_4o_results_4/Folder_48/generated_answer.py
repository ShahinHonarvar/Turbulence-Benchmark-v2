def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_string, 2)
    fib_198 = fibonacci(198)
    return decimal_num % fib_198 == 0