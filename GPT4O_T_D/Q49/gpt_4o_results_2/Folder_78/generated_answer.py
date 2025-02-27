def if_decimal_is_divisible(binary_string):

    def fibonacci_num(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    fib_115 = fibonacci_num(115)
    return decimal_number % fib_115 == 0