def if_decimal_is_divisible(binary_str):

    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n - 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_str, 2)
    return decimal % fib(88) == 0