def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_rep, 2)
    fib_number = fibonacci(119)
    return decimal_number % fib_number == 0