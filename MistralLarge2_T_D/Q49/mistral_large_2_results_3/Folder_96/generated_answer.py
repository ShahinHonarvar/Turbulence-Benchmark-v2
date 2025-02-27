def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib47 = fibonacci(47)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib47 == 0