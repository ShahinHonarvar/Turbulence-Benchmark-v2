def if_decimal_is_divisible(binary):

    def binary_to_decimal(b):
        decimal = 0
        for i in range(len(b)):
            decimal = decimal + int(b[i]) * 2 ** (len(b) - 1 - i)
        return decimal

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    return binary_to_decimal(binary) % fibonacci(163) == 0