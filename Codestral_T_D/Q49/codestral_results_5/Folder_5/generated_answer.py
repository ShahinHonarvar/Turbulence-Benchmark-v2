def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return decimal % fibonacci(85) == 0