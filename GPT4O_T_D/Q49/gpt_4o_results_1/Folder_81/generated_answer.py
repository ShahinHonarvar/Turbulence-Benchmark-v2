def if_decimal_is_divisible(binary_string):

    def fibonacci_nth(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    fib_97 = fibonacci_nth(97)
    return decimal_number % fib_97 == 0