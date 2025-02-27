def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_value = binary_to_decimal(binary_str)
    fib_39th = fibonacci(39)
    return decimal_value % fib_39th == 0