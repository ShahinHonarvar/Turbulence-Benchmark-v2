def if_decimal_is_divisible(binary_rep):

    def fibonacci_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_integer = int(binary_rep, 2)
    fib_178 = fibonacci_number(178)
    return decimal_integer % fib_178 == 0