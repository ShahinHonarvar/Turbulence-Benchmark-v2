def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    seventh_fibonacci = fibonacci(7)
    return decimal % seventh_fibonacci == 0