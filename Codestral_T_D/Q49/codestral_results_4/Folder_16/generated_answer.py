def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(bin_str, 2)
    fib_128 = fib(128)
    return decimal % fib_128 == 0