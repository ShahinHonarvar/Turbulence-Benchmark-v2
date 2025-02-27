def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_47 = fibonacci_number(47)
    return decimal_value % fib_47 == 0