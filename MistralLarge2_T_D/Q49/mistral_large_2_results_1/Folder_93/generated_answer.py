def if_decimal_is_divisible(binary_str):

    def fibonacci_number(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    fib_59 = fibonacci_number(59)
    return decimal_number % fib_59 == 0