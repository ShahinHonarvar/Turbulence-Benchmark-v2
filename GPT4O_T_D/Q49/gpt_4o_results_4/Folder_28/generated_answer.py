def if_decimal_is_divisible(binary_string):

    def fibonacci_n(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return b
    fib_104th = fibonacci_n(104)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_104th == 0