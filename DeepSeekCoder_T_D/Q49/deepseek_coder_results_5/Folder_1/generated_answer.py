def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = binary_to_decimal(binary_str)
    fib_90 = fibonacci(90)
    return decimal_value % fib_90 == 0