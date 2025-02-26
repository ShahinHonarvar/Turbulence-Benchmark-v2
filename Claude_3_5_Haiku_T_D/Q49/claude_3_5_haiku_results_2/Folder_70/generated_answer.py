def if_decimal_is_divisible(binary_str):

    def fibonacci_137():
        a, b = (0, 1)
        for _ in range(136):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_137 = fibonacci_137()
    return decimal_num % fib_137 == 0