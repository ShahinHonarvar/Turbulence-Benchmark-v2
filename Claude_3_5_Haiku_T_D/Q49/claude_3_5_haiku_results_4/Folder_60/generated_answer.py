def if_decimal_is_divisible(binary_string):

    def fibonacci_108():
        a, b = (0, 1)
        for _ in range(106):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    fib_number = fibonacci_108()
    return decimal_value % fib_number == 0