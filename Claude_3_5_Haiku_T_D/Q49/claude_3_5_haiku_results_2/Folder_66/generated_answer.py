def if_decimal_is_divisible(binary_str):

    def fib_number(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_str, 2)
    fibonacci_120 = fib_number(120)
    return decimal_value % fibonacci_120 == 0