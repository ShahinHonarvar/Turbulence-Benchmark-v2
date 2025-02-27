def if_decimal_is_divisible(binary_str):

    def nth_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal_value = int(binary_str, 2)
    fibonacci_120th = nth_fibonacci(120)
    return decimal_value % fibonacci_120th == 0