def if_decimal_is_divisible(binary_str):

    def fibonacci_49th():
        a, b = (0, 1)
        for _ in range(47):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_49 = fibonacci_49th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_49 == 0