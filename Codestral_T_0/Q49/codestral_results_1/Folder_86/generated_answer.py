def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal = binary_to_decimal(binary_str)
    fib_135 = fibonacci(135)
    return decimal % fib_135 == 0