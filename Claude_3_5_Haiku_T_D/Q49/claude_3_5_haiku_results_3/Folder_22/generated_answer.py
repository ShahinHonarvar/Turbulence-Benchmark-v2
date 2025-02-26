def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        fib_a, fib_b = (0, 1)
        for _ in range(2, n + 1):
            fib_a, fib_b = (fib_b, fib_a + fib_b)
        return fib_b
    decimal_number = int(binary_string, 2)
    fib_20 = fibonacci(20)
    return decimal_number % fib_20 == 0