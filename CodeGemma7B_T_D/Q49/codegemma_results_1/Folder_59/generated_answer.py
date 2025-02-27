def if_decimal_is_divisible(binary_representation):

    def fibonacci_sequence(n):
        if n <= 1:
            return n
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
    decimal = int(binary_representation, 2)
    fib_74 = fibonacci_sequence(74)
    return decimal % fib_74 == 0