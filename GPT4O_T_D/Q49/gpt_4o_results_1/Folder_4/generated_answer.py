def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    binary_number = int(binary_str, 2)
    fib_number = fibonacci(118)
    return binary_number % fib_number == 0