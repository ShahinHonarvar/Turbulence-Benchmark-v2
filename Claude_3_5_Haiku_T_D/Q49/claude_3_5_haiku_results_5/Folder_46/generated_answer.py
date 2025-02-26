def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal_value = binary_to_decimal(binary_str)
    fib_139 = fibonacci_number(139)
    return decimal_value % fib_139 == 0