def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def bin_to_dec(binary_str):
        return int(binary_str, 2)
    decimal = bin_to_dec(binary_str)
    fib_85 = fib(85)
    return decimal % fib_85 == 0