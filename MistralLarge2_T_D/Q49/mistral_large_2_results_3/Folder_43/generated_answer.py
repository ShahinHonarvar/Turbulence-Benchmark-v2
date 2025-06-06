def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_representation, 2)
    fibonacci_77th = fibonacci(77)
    return decimal_number % fibonacci_77th == 0