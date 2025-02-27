def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    decimal = int(binary_representation, 2)
    nth_fibonacci = fibonacci(105)
    return decimal % nth_fibonacci == 0