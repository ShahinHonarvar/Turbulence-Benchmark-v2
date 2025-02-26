def if_decimal_is_divisible(binary_string):

    def fibonacci_110th():
        a, b = (0, 1)
        for _ in range(109):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_110 = fibonacci_110th()
    decimal_number = binary_to_decimal(binary_string)
    return decimal_number % fib_110 == 0