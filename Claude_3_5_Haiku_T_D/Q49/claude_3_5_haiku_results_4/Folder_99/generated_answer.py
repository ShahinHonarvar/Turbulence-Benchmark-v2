def if_decimal_is_divisible(binary_string):

    def fibonacci_109():
        a, b = (0, 1)
        for _ in range(108):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    fib_109_value = fibonacci_109()
    return decimal_value % fib_109_value == 0