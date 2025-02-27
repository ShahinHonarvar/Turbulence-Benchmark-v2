def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    num = int(binary_str, 2)
    fib_47 = fib(47)
    return num % fib_47 == 0