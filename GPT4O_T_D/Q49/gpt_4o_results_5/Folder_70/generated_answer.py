def if_decimal_is_divisible(binary_string):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    fibonacci_137th = fib(137)
    return decimal_number % fibonacci_137th == 0