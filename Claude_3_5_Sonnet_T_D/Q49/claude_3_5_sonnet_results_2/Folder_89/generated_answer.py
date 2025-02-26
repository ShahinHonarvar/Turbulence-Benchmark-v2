def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        fib_prev, fib_curr = (0, 1)
        for _ in range(2, n + 1):
            fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
        return fib_curr
    decimal_number = int(binary_string, 2)
    fib_126 = fibonacci(126)
    return decimal_number % fib_126 == 0