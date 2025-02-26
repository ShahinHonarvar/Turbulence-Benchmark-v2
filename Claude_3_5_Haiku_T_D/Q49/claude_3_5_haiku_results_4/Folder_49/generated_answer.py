def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    decimal_value = binary_to_decimal(binary_str)
    fib_95 = fibonacci_number(95)
    return decimal_value % fib_95 == 0