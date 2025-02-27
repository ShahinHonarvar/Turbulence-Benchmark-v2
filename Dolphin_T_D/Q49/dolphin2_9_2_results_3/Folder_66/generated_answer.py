def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return decimal_number % nth_fibonacci(120) == 0