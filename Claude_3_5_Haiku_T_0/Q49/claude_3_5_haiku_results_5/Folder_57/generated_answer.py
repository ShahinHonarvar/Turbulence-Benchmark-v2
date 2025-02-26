def if_decimal_is_divisible(binary_str):

    def fibonacci_80th():
        a, b = (0, 1)
        for _ in range(79):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_80 = fibonacci_80th()
    return decimal_num % fib_80 == 0