def if_decimal_is_divisible(binary_string):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n = fib(160)
    dec = int(binary_string, 2)
    return dec % n == 0