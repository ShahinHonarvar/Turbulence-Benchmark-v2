def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fifteenth_fibonacci = fibonacci(15)
    return decimal_num % fifteenth_fibonacci == 0