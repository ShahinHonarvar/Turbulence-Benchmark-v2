def if_decimal_is_divisible(binary):

    def fibonacci(n):
        a, b = (0, 1)
        while n > 0:
            a, b = (b, a + b)
            n -= 1
        return a
    n = fibonacci(178)
    return int(binary, 2) % n == 0