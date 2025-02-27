def if_decimal_is_divisible(binary):

    def fib(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal = int(binary, 2)
    return decimal % fib(150) == 0