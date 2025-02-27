def if_decimal_is_divisible(binary_string):

    def get_fibonacci_number(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    fibonacci_105th = get_fibonacci_number(105)
    return decimal_number % fibonacci_105th == 0