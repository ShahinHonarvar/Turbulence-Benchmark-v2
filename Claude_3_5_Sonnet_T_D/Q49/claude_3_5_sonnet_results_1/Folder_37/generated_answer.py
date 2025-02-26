def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fib_46 = fibonacci(46)
    decimal = int(binary_string, 2)
    return decimal % fib_46 == 0