def if_decimal_is_divisible(binary_str):

    def fibonacci_24th():
        a, b = (0, 1)
        for _ in range(23):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_24_num = fibonacci_24th()
    return decimal_num % fib_24_num == 0