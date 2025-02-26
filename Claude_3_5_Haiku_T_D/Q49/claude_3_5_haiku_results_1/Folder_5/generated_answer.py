def if_decimal_is_divisible(binary_str):

    def fibonacci_85():
        a, b = (0, 1)
        for _ in range(84):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    fib_85 = fibonacci_85()
    return decimal % fib_85 == 0