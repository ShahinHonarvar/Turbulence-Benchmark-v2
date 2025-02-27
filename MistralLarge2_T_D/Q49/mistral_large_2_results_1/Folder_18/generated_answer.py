def if_decimal_is_divisible(binary_representation):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_representation, 2)
    fibonacci_199th = nth_fibonacci(199)
    return decimal % fibonacci_199th == 0