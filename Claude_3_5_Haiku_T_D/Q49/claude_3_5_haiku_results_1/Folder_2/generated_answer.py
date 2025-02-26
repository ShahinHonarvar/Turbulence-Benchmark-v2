def if_decimal_is_divisible(binary_string):

    def fibonacci_125():
        a, b = (0, 1)
        for _ in range(124):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_string, 2)
    fib_125 = fibonacci_125()
    return decimal_num % fib_125 == 0