def if_decimal_is_divisible(binary_str):

    def fibonacci_at_index(n):
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
    decimal_num = binary_to_decimal(binary_str)
    fib_95 = fibonacci_at_index(95)
    return decimal_num % fib_95 == 0