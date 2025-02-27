def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_99 = fib(99)
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_99 == 0