def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_95 = 31940434634990099905

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_generator = fibonacci()
    for _ in range(95):
        next(fib_generator)
    return decimal % fib_95 == 0