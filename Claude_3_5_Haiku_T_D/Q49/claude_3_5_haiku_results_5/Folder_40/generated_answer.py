def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary):
        return int(binary, 2)

    def fibonacci_sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal_value = binary_to_decimal(binary_str)
    fourth_fibonacci = fibonacci_sequence(4)
    return decimal_value % fourth_fibonacci == 0