def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_string, 2)
    fib_90 = fibonacci(90)
    return decimal_number % fib_90 == 0