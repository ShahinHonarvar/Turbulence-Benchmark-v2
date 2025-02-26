def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_string, 2)
    fib_130 = fibonacci(130)
    return decimal_num % fib_130 == 0