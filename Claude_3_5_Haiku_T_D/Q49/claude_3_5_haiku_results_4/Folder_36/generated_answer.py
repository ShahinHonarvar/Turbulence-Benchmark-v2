def if_decimal_is_divisible(binary_str):

    def fibonacci_at_index(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_str, 2)
    fib_150 = fibonacci_at_index(150)
    return decimal_value % fib_150 == 0