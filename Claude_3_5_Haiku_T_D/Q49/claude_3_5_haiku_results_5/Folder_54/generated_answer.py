def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_34 = fibonacci(34)
    return decimal_num % fib_34 == 0