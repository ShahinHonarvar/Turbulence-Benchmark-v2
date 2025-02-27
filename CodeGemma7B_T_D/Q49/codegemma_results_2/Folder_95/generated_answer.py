def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_168 = fibonacci(168)
    if decimal_representation % fibonacci_168 == 0:
        return True
    else:
        return False