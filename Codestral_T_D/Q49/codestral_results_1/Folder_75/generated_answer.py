def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_str, 2)
    fibo_189 = fibonacci(189)
    return decimal % fibo_189 == 0