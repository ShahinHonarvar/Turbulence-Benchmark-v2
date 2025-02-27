def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)

    def nth_fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    return decimal % nth_fibonacci(56) == 0