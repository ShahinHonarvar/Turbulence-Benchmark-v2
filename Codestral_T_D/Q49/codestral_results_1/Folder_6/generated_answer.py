def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    num = int(bin_str, 2)
    fib185 = fib(185)
    return num % fib185 == 0