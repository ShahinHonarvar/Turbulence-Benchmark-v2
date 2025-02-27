def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)

    def get_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib174 = get_fibonacci(174)
    if decimal % fib174 == 0:
        return True
    else:
        return False