def if_decimal_is_divisible(binary_string):

    def fibonacci_number(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_118 = fibonacci_number(118)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_118 == 0