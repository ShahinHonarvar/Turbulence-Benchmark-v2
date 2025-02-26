def if_decimal_is_divisible(binary_str):

    def fib_90th():
        a, b = (0, 1)
        for _ in range(89):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_90 = fib_90th()
    return decimal_num % fib_90 == 0