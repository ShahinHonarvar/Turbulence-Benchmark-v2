def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            yield a
            a, b = (b, a + b)
    fib_sequence = list(fibonacci(20))
    divisor = fib_sequence[18]
    decimal = int(binary_string, 2)
    return decimal % divisor == 0