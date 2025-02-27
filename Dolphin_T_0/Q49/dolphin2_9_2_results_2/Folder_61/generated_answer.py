def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)

    def fib(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n):
                a, b = (b, a + b)
            return b
    fib_76 = fib(76)
    if decimal_value % fib_76 == 0:
        return True
    else:
        return False