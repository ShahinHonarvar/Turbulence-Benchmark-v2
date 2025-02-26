def if_decimal_is_divisible(binary_str):

    def fibonacci_108():
        if 108 == 0:
            return 0
        if 108 == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, 109):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_str, 2)
    fib_108 = fibonacci_108()
    return decimal_value % fib_108 == 0