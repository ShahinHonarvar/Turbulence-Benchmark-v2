def if_decimal_is_divisible(binary_string):

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n - 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_string, 2)
    fib_180 = fib(180)
    return decimal % fib_180 == 0