def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_string, 2)
    fibonacci_120 = fibonacci(120)
    return decimal_num % fibonacci_120 == 0