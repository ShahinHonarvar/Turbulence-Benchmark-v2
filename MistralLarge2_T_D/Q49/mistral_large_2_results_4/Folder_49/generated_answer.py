def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal_value = int(binary_str, 2)
    fib_95 = fibonacci(95)
    return decimal_value % fib_95 == 0