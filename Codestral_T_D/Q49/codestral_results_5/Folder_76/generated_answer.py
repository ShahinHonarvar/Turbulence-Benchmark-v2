def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n - 1):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    return decimal % fibonacci(188) == 0