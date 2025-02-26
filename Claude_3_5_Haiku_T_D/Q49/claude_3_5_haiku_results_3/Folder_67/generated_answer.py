def if_decimal_is_divisible(binary_str):

    def fibonacci_107():
        a, b = (0, 1)
        for _ in range(106):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_107 = fibonacci_107()
    return decimal_num % fib_107 == 0