def if_decimal_is_divisible(binary_str):

    def fibonacci_109():
        a, b = (0, 1)
        for _ in range(108):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_109 = fibonacci_109()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_109 == 0