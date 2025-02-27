def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec_value = int(binary_string, 2)
    fib_189 = fibonacci(189)
    return dec_value % fib_189 == 0