def if_decimal_is_divisible(binary_str):

    def fib_60():
        a, b = (0, 1)
        for _ in range(59):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    return decimal % fib_60() == 0