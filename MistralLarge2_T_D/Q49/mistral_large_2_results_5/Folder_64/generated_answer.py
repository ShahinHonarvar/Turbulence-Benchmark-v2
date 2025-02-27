def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal = int(bin_str, 2)
    return decimal % fibonacci(10) == 0