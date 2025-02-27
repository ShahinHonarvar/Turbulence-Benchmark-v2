def if_decimal_is_divisible(binary_rep):

    def to_decimal(binary_rep):
        return int(binary_rep, 2)

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    return to_decimal(binary_rep) % fibonacci(54) == 0