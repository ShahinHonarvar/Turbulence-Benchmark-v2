def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        fib_prev, fib_curr = (0, 1)
        for _ in range(2, n + 1):
            fib_prev, fib_curr = (fib_curr, fib_prev + fib_curr)
        return fib_curr
    decimal_num = int(binary_str, 2)
    fib_125 = fibonacci_number(125)
    return decimal_num % fib_125 == 0