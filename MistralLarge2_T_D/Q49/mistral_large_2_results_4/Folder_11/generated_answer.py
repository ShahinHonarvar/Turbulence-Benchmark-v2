def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec_num = int(binary_str, 2)
    fib_16th = fibonacci(16)
    return dec_num % fib_16th == 0