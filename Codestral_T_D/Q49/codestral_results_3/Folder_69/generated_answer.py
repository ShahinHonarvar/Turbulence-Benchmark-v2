def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(bin_str, 2)
    return decimal_num % fib(170) == 0