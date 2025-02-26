def if_decimal_is_divisible(binary_string):

    def fibonacci_115th():
        a, b = (0, 1)
        for _ in range(114):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    fib_115 = fibonacci_115th()
    return decimal_value % fib_115 == 0