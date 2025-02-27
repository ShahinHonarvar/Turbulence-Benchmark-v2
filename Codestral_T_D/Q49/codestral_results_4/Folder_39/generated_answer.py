def if_decimal_is_divisible(binary):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary, 2)
    return decimal % fib(15) == 0