def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_string, 2)
    fib_19th_number = fibonacci(19)
    return decimal_number % fib_19th_number == 0