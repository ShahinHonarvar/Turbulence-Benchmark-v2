def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fib_69 = fibonacci(69)
    decimal = int(binary_string, 2)
    return decimal % fib_69 == 0