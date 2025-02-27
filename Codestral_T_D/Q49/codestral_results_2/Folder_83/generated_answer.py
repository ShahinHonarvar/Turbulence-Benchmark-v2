def if_decimal_is_divisible(binary):

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    binary = int(binary, 2)
    return binary % fibonacci(60) == 0