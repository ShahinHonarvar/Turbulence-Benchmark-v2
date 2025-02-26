def if_decimal_is_divisible(binary_str):

    def fibonacci_6th():
        a, b = (0, 1)
        for _ in range(5):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_str, 2)
    fib_6th = fibonacci_6th()
    return decimal_value % fib_6th == 0