def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_9 = fib(9)
    return decimal % fib_9 == 0