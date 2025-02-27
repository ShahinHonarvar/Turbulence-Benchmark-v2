def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n = int(binary_string, 2)
    fib_78 = fibonacci(78)
    return n % fib_78 == 0