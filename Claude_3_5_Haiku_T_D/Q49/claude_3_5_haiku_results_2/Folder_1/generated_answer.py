def if_decimal_is_divisible(binary_str):

    def fibonacci_90th():
        a, b = (0, 1)
        for _ in range(89):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_90 = fibonacci_90th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_90 == 0