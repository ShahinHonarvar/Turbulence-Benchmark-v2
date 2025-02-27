def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n - 1):
                a, b = (b, a + b)
            return b
    decimal_value = int(binary_str, 2)
    fib_34 = fibonacci_number(34)
    return decimal_value % fib_34 == 0