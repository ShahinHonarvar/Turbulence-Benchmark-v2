def if_decimal_is_divisible(binary_str):

    def fibonacci_99th():
        a, b = (0, 1)
        for _ in range(98):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_99 = fibonacci_99th()
    return decimal_num % fib_99 == 0