def if_decimal_is_divisible(binary_str):

    def fibonacci_196():
        a, b = (0, 1)
        for _ in range(195):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    fib_196 = fibonacci_196()
    return decimal % fib_196 == 0