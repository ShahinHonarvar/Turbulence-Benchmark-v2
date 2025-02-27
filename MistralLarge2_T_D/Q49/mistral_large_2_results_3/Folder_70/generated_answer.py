def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_137 = fibonacci_number(137)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_137 == 0