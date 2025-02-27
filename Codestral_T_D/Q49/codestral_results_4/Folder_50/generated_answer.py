def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    return decimal % fibonacci(119) == 0