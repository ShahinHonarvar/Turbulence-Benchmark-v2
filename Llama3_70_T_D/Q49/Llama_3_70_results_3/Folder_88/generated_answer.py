def if_decimal_is_divisible(binary_string):

    def fibonacci():
        a, b = (0, 1)
        for _ in range(49):
            yield a
            a, b = (b, a + b)
    decimal = int(binary_string, 2)
    fib = list(fibonacci())[-1]
    return decimal % fib == 0