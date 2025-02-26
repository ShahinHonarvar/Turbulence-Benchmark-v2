def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_90 = fibonacci(90)
    decimal_value = binary_to_decimal(binary_string)
    return decimal_value % fib_90 == 0