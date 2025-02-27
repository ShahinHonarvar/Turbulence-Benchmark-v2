def if_decimal_is_divisible(binary_representation):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_representation, 2)
    fibonacci_174 = nth_fibonacci(174)
    return decimal_value % fibonacci_174 == 0