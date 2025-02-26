def if_decimal_is_divisible(binary_string):

    def fibonacci_118th():
        a, b = (0, 1)
        for _ in range(117):
            a, b = (b, a + b)
        return b
    decimal_number = int(binary_string, 2)
    fib_118 = fibonacci_118th()
    return decimal_number % fib_118 == 0