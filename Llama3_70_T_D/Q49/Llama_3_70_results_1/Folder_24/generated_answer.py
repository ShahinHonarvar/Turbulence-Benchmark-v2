def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        for _ in range(56):
            yield a
            a, b = (b, a + b)
    fib_gen = fibonacci()
    divisor = next(fib_gen)
    decimal = int(binary_str, 2)
    return decimal % divisor == 0