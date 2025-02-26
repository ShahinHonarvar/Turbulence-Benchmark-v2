def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        fib_prev, fib_curr = (0, 1)
        for _ in range(2, n + 1):
            fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
        return fib_curr
    decimal = int(binary_str, 2)
    ninth_fibonacci = fibonacci(9)
    return decimal % ninth_fibonacci == 0