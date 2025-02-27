def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n < 2:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    dec_num = int(binary_str, 2)
    fib_num = fibonacci(53)
    return dec_num % fib_num == 0