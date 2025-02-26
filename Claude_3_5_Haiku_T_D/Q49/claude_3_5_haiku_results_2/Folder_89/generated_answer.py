def if_decimal_is_divisible(binary_string):

    def fibonacci_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    fibonacci_126 = fibonacci_number(126)
    return decimal_value % fibonacci_126 == 0