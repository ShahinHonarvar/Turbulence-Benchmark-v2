def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return decimal % fibonacci(4) == 0