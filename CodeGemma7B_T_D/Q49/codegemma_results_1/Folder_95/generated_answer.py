def if_decimal_is_divisible(binary_representation):

    def nth_fibonacci(n):
        first, second = (0, 1)
        for _ in range(n):
            first, second = (second, first + second)
        return first
    decimal_value = int(binary_representation, 2)
    fibonacci_value = nth_fibonacci(168)
    return decimal_value % fibonacci_value == 0