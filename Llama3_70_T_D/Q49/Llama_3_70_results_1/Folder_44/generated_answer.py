def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n):
                a, b = (b, a + b)
            return a
    decimal = int(binary_string, 2)
    fib_159 = fibonacci(159)
    return decimal % fib_159 == 0