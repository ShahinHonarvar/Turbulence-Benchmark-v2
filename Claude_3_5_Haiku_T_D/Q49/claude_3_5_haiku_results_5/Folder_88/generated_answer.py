def if_decimal_is_divisible(binary_string):

    def fibonacci_49th():
        if n == 0:
            return 0
        a, b = (0, 1)
        for _ in range(48):
            a, b = (b, a + b)
        return b
    n = int(binary_string, 2)
    fib_number = fibonacci_49th()
    return n % fib_number == 0