def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    decimal_value = int(binary_representation, 2)
    return decimal_value % fibonacci(27) == 0