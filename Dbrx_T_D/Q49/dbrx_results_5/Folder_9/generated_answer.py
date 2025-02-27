def if_decimal_is_divisible(bin_repr_decimal_int):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n):
                a, b = (b, a + b)
            return b
    decimal_int = int(bin_repr_decimal_int, 2)
    return decimal_int % fibonacci(68) == 0