def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        fib_prev, fib_curr = (0, 1)
        for _ in range(2, n + 1):
            fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
        return fib_curr
    seventh_fibonacci = fibonacci(7)
    return decimal % seventh_fibonacci == 0