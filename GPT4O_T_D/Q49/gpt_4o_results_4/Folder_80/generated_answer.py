def if_decimal_is_divisible(binary_string):

    def fibonacci_n(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n_decimal = int(binary_string, 2)
    fibonacci_179 = fibonacci_n(179)
    return n_decimal % fibonacci_179 == 0