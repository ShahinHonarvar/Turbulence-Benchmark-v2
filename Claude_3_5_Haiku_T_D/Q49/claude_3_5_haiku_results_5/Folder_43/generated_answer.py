def if_decimal_is_divisible(binary_str):

    def fibonacci_77():
        a, b = (0, 1)
        for _ in range(76):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_str, 2)
    fib_77 = fibonacci_77()
    return decimal_number % fib_77 == 0