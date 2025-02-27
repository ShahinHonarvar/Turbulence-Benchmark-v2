def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_80 = fibonacci(80)
    decimal = int(binary_string, 2)
    return decimal % fibonacci_80 == 0