def if_decimal_is_divisible(binary_str):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fib_135 = nth_fibonacci(135)
    return decimal % fib_135 == 0