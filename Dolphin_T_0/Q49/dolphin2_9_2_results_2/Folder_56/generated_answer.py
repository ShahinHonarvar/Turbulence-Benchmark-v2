def if_decimal_is_divisible(binary_representation):

    def fib_n(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal = int(binary_representation, 2)
    fib84 = fib_n(84)
    if decimal % fib84 == 0:
        return True
    else:
        return False