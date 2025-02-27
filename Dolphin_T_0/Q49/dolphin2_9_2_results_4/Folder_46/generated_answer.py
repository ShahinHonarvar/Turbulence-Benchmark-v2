def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    dec = int(binary_string, 2)
    fib_139 = fibonacci(139)
    return dec % fib_139 == 0