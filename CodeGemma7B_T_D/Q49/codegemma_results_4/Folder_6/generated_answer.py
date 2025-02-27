def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_0, fib_1 = (0, 1)
        for _ in range(2, n + 1):
            fib_0, fib_1 = (fib_1, fib_0 + fib_1)
        return fib_1
    decimal_int = int(binary_str, 2)
    fibonacci_number = fibonacci(185)
    return decimal_int % fibonacci_number == 0