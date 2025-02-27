def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_59th = fibonacci(59)
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_59th == 0