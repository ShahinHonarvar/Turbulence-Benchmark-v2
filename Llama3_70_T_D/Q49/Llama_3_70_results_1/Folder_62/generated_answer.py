def if_decimal_is_divisible(binary_string):

    def generate_fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b
    fibonacci_130 = generate_fibonacci(130)
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_130 == 0