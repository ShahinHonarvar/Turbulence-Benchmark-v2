def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return b
    n = int(binary_str, 2)
    return n % fibonacci(179) == 0